from environs import Env

#  Берется с https://my.telegram.org/auth

env = Env()
env.read_env()

api_id = env.int("28303272")
api_hash = env.str("39bb8e386ca54538ae031dd514fb6552")
phone_number = env.str("+393714099692")
