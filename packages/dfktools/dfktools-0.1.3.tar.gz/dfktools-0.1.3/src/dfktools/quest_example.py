import logging
import sys
import time
from web3 import Web3
import quests.professions.fishing as fishing
import quests.professions.gardening as gardening
import quests.quest_v2 as quest_v2, quests.quest_core_v2 as quest_core_v2, quests.quest_v1 as quest_v1
import quests.utils.utils as quest_utils

ZERO_ADDRESS = '0x0000000000000000000000000000000000000000'

if __name__ == "__main__":
    log_format = '%(asctime)s|%(name)s|%(levelname)s: %(message)s'

    logger = logging.getLogger("DFK-quest")
    logger.setLevel(logging.DEBUG)
    logging.basicConfig(level=logging.INFO, format=log_format, stream=sys.stdout)

    serendale_rpc_server = 'https://api.harmony.one'
    crystalvale_rpc_server = 'https://subnets.avax.network/defi-kingdoms/dfk-chain/rpc'
    logger.info("Using RPC servers " + serendale_rpc_server + ", " + crystalvale_rpc_server)

    private_key = None  # set private key
    gas_price_gwei_serendale = 115
    gas_price_gwei_crystalvale = {'maxFeePerGas': 2, 'maxPriorityFeePerGas': 2}  # EIP-1559
    tx_timeout = 30
    w3_serendale = Web3(Web3.HTTPProvider(serendale_rpc_server))
    w3_crystalvale = Web3(Web3.HTTPProvider(crystalvale_rpc_server))
    account_address = w3_serendale.eth.account.privateKeyToAccount(private_key).address

    '''
    All quest but gardening & mining should be started with V2
    '''

    # Fishing in Crystalvale
    questV2 = quest_v2.Quest(quest_core_v2.CRYSTALVALE_CONTRACT_ADDRESS, crystalvale_rpc_server, logger)
    quest_contract = fishing.CRYSTALVALE_QUEST_CONTRACT_ADDRESS
    my_heroes_id = [1, 2, 3, 4]
    attempts = 3
    level = 1
    questV2.start_quest(quest_contract, my_heroes_id, attempts, level, private_key, w3_crystalvale.eth.getTransactionCount(account_address), gas_price_gwei_crystalvale, tx_timeout)
    quest_info = quest_utils.human_readable_quest(questV2.get_hero_quest(my_heroes_id[0]))

    logger.info(
        "Waiting " + str(quest_info['completeAtTime'] - time.time()) + " secs to complete quest " + str(quest_info))
    while time.time() < quest_info['completeAtTime']:
        time.sleep(2)

    tx_receipt = questV2.complete_quest(my_heroes_id[0], private_key, w3_crystalvale.eth.getTransactionCount(account_address), gas_price_gwei_crystalvale, tx_timeout)
    quest_result = questV2.parse_complete_quest_receipt(tx_receipt)
    quest_rewards = quest_utils.human_readable_quest_results(quest_result, very_human=True)
    logger.info("Rewards: {}".format(str(quest_rewards)))

    # Gardening in Serendale
    pool_id = 0  # See gardens.master_gardener
    questV1 = quest_v1.Quest(serendale_rpc_server, logger)
    quest_data = (pool_id, 0, 0, 0, 0, 0, '', '', ZERO_ADDRESS, ZERO_ADDRESS, ZERO_ADDRESS, ZERO_ADDRESS)
    my_gardener_heroes_id = [5]
    attempts = 1
    questV1.start_quest_with_data(gardening.SERENDALE_QUEST_CONTRACT_ADDRESS, quest_data, my_gardener_heroes_id, attempts, private_key, w3_serendale.eth.getTransactionCount(account_address), gas_price_gwei_serendale, tx_timeout)
    quest_info = quest_utils.human_readable_quest(questV1.get_hero_quest(my_heroes_id[0]))

    logger.info(
        "Waiting " + str(quest_info['completeAtTime'] - time.time()) + " secs to complete gardening quest " + str(quest_info))
    while time.time() < quest_info['completeAtTime']:
        time.sleep(2)

    tx_receipt = questV1.complete_quest(my_gardener_heroes_id[0], private_key, w3_serendale.eth.getTransactionCount(account_address),
                                        gas_price_gwei_serendale, tx_timeout)
    quest_result = questV1.parse_complete_quest_receipt(tx_receipt)
    quest_rewards = quest_utils.human_readable_quest_results(quest_result, very_human=True)
    logger.info("Rewards: {}".format(str(quest_rewards)))