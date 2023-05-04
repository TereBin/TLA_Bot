import time

err_txt_path = "../data/err_log.txt"


async def err_logging(err_data):
    err_data = str(err_data)
    with open(err_txt_path, 'a') as f:
        err_log = "[" + str(time.strftime('%m/%d %H:%M', time.localtime(time.time()))) + "] " + "new error : \n" + err_data + "\n\n"
        f.write(err_log)
    print("error occurred")
    print(err_data, "\n")
