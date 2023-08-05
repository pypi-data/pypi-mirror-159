import json
import time
from abc import ABC, abstractmethod
from os import path

from empiric.core.const import NETWORK, ORACLE_CONTROLLER_ADDRESS
from nile.signer import Signer
from starknet_py.contract import Contract, ContractData, ContractFunction
from starknet_py.net import Client
from starkware.crypto.signature.signature import sign
from starkware.starknet.public.abi import get_selector_from_name

MAX_FEE = 0
FEE_SCALING_FACTOR = 1.1  # estimated fee is multiplied by this to set max_fee


class EmpiricBaseClient(ABC):
    def __init__(
        self,
        account_private_key,
        account_contract_address,
        network=None,
        oracle_controller_address=None,
        n_retries=None,
    ):
        if network is None:
            network = NETWORK
        if oracle_controller_address is None:
            oracle_controller_address = ORACLE_CONTROLLER_ADDRESS

        self.network = network
        self.oracle_controller_address = oracle_controller_address
        self.oracle_controller_contract = None
        self.account_contract_address = account_contract_address
        self.account_contract = None

        assert type(account_private_key) == int, "Account private key must be integer"
        self.account_private_key = account_private_key
        self.signer = Signer(self.account_private_key)

        self.client = Client(self.network, n_retries=n_retries)

    @abstractmethod
    async def _fetch_contracts(self):
        pass

    async def _fetch_base_contracts(self):
        if self.oracle_controller_contract is None:
            self.oracle_controller_contract = await Contract.from_address(
                self.oracle_controller_address,
                self.client,
            )

        if self.account_contract is None:
            self.account_contract = await Contract.from_address(
                self.account_contract_address, self.client
            )

    async def get_eth_balance(self):
        if self.network == "testnet":
            eth_address = (
                0x049D36570D4E46F48E99674BD3FCC84644DDD6B96F7C741B1562B82F9E004DC7
            )
        else:
            raise NotImplementedError(
                "EmpiricBaseClient.get_eth_balance: Unknown network type"
            )

        with open(path.join(path.dirname(__file__), "abi/ERC20.json"), "r") as f:
            erc20_abi = json.load(f)
        contract_data = ContractData.from_abi(eth_address, erc20_abi)
        balance_of_abi = [a for a in erc20_abi if a["name"] == "balanceOf"][0]
        balance_of_function = ContractFunction(
            "balanceOf", balance_of_abi, contract_data, self.client
        )

        result = await balance_of_function.call(self.account_contract_address)

        return result.balance

    async def send_transaction(
        self, to_contract, selector_name, calldata, max_fee=None
    ):
        return await self.send_transactions(
            [(to_contract, selector_name, calldata)], max_fee
        )

    async def send_transactions(self, calls, max_fee=None):
        # Format data for submission
        call_array = []
        offset = 0
        for i in range(len(calls)):
            call_array.append(
                {
                    "to": calls[i][0],
                    "selector": get_selector_from_name(calls[i][1]),
                    "data_offset": offset,
                    "data_len": len(calls[i][2]),
                }
            )
            offset += len(calls[i][2])
        calldata = [x for call in calls for x in call[2]]

        # Estimate fee
        with open(path.join(path.dirname(__file__), "abi/Account.json"), "r") as f:
            account_abi = json.load(f)
        contract_data = ContractData.from_abi(
            self.account_contract_address, account_abi
        )
        execute_abi = [a for a in account_abi if a["name"] == "__execute__"][0]
        execute_function = ContractFunction(
            "__execute__", execute_abi, contract_data, self.client
        )
        nonce = int(time.time())
        prepared = execute_function.prepare(
            call_array=call_array,
            calldata=calldata,
            nonce=nonce,
        )
        signature = sign(prepared.hash, self.account_private_key)
        # TODO: Change to using AccountClient once estimate_fee is fixed there
        tx = prepared._make_invoke_function(signature=signature)
        estimate = await prepared._client.estimate_fee(tx=tx)

        max_fee_estimate = int(estimate * FEE_SCALING_FACTOR)
        max_fee = (
            max_fee_estimate if max_fee is None else min(max_fee_estimate, max_fee)
        )

        # Submit transaction with fee
        prepared_with_fee = execute_function.prepare(
            call_array=call_array,
            calldata=calldata,
            nonce=nonce,
            max_fee=max_fee,
        )
        signature = sign(prepared_with_fee.hash, self.account_private_key)
        invocation = await prepared_with_fee.invoke(signature, max_fee=max_fee)

        return invocation
