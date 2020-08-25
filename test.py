from PyTier import get_tier

try:
    while True:
        x = input("Character name>> ")
        print(get_tier(x))
except KeyboardInterrupt:
    pass
   