import logging
logging.basicConfig(level=logging.WARN,
                    filename="log.txt",
                    format="%(asctime)s=>%(levelname)s==>%(message)s")
logging.info("program started")
a=input("enter a value:")
logging.info("a vlaue entered")
b=input("Enter b value:")
logging.info("b value entered.")
logging.debug(f"before converting: a={a},b={b}")
try:
    a=float(a)
    logging.info("a value converted.")
    b=float(b)
    logging.info("b value converted")
    logging.debug(f"after converting: a={a},b={b}")
    res=a/b
    r = f"result={res}"
    print(r)
    logging.debug(r)
except ZeroDivisionError as err:
    error = "ERROR: Not expecting zero for b"
    print(error)
    logging.error(error)
except ValueError as err:
    error = "ERROR: Excpeting only digits"
    print(error)
    logging.error(error)
except Exception as err:
    error = "ERROR:%s"%err
    print(error)
    logging.error(error)
logging.info("program ended")