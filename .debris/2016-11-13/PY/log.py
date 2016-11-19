class Log():
    import logging
    def log_in(Log):
        logging.basicConfig(format='%(asctime)s %(message)s')
        logging.basicConfig(filename='Log_In.log', level=logging.INFO)
        logging.info([Log])

    def log_out(PRINT):
            n = "Output"
            e = "txt"
            p = ".../UI/Output"
            ndatei = open(p+"/"+n+"."+e,'w')
            ndatei.write(PRINT)
            ndatei.close()
