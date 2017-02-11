import time
import datetime
import csv
import os
import json
import sys
import logging
import send2trash

logging.basicConfig(filename='program_Log.txt', level=logging.INFO, format=' %(asctime)s -  %(levelname)s -  %(message)s')

MASTER_PASSWORD = 'minjun5627'
MASTERUSERNAME = 'minjun'
MASTERUSERPASSWORD = '2005'
#os.chdir('/SE_point_severce/')

def setup():
    logging.info('function info:"setup"function in activate state.')
    print('---SE---')
    print('••••loading modules...')
    time.sleep(1)
    print('••••starting program...')
    time.sleep(1)
    print('---------------------------------------------------------------------')
    logging.info('function info:"setup"function termited.')


def master():
    logging.warning('master status: master function starting...')
    print('---SE master mode---')
    USERIN = input('master_kor>>:')
    if USERIN == 'charge points' or USERIN == 'charge':
        logging.info('master status: master request charge points.')
        usernameIn = input('please write the user name you want to charge points:')
        try:
            for file in os.listdir('./'):
                if file.strip('.csv') == usernameIn:
                    userFile = open(usernameIn + '.csv', 'r')
                    userName = usernameIn.strip('.csv')
                    userFileRead = userFile.readlines()
                    user_password = str(userFileRead[0].strip('\n'))
                    user_points = int(userFileRead[1])
                    userFile.close()

            USERpoints = input('please write the points you want to charge:')
            user_FileE = open(str(usernameIn) + '.csv', 'w')
            user_FileE.write(user_password + '\n')
            user_pluse_points = user_points + int(USERpoints)
            user_points = str(user_pluse_points)
            user_FileE.write(user_points)
            user_FileE.close()
        except:
            print('No user %s. please try again.' % (usernameIn))

    if USERIN == 'del user':
        logging.info('master status: del user.')
        USERIN = input('please write the user name you want to del:')
        for file in os.listdir('./'):
            if file.strip('.csv') == USERIN:
                delfile = file
        try:
            send2trash.send2trash(os.path.join(os.getcwd(), delfile))
        except:
            print('No user %s. please try again.' % (USERIN))




def setup_login():
    logging.info('function info:"setup_login"function in activate state.')
    while True:
        USERINPUT = input('>user공용_kor:')
        if USERINPUT == 'login':
            logging.info('function info:user logining...')
            Id = input('ID:')
            for file in os.listdir('./'):
                if file.strip('.csv') == Id:
                    userFile = open(str(file), 'r')
                    userName = file.strip('.csv')
                    userFileRead = userFile.readlines()
                    user_password = str(userFileRead[0].strip('\n'))
                    user_points = int(userFileRead[1])


            try:

                while True:
                    logging.info('user state: writing password.')
                    userINPassword = input('Password:')
                    if str(userINPassword) == user_password:
                        logging.warning('security state: user %s logined' % (userName))
                        print('Access OK.')
                        print('Changing mode to private mode...')
                        logging.info('user state:Changing mode to private mode.')
                        return userFile, userName, userFileRead, user_password, user_points
                    else:
                        print('Your password or user ID is worng.')
                        time.sleep(0.2)
                        print('Please try again.')
                        time.sleep(0.2)
                        logging.info('user state:user login failed.')
                        break
            except:
                print('Your password or user ID is worng.')
                time.sleep(0.2)
                print('Please try again.')
                logging.info('user state:user login failed.')
                time.sleep(0.2)

        elif USERINPUT == 'make user' or USERINPUT == 'makeUser':
            logging.warning('user state: makeing user.')
            NewuserName = input('New ID:')
            NewuserPassword = input('New password:')
            while True:

                INPUT = input('comfrim password:')
                if INPUT == NewuserPassword:
                    break
                else:
                    print('The password you wrote is not same.')
                    time.sleep(0.2)
                    print('please try again.')
                    time.sleep(0.2)

            print('makeing new user...')
            NewuserFile = open(str(NewuserName) + '.csv', 'w')
            NewuserFile.write(str(NewuserPassword) + '\n')
            NewuserFile.write('200')
            NewuserFile.close()
            print('User makeing complete!')
            logging.info('user state:user makeing complete!')
            time.sleep(0.2)
            print('Please Relogin.')

        elif USERINPUT == 'terminat' or USERINPUT == 'OFF':
            logging.info('system status:system closeing.')
            print('system closeing...')
            time.sleep(1)
            print('Goodby~!')
            logging.info('system closed.')
            sys.exit(10)

        elif USERINPUT == 'help' or USERINPUT == 'Help':
            logging.info('user status: Requested help.')
            print('commands:')
            print('••login:To login to the program.')
            print('••make user:To make a New user.')
            print('••terminat:To close system.')

        elif USERINPUT == 'login to master mode':
            logging.warning('user status: logining to master mode...')
            USERINPUT = input('Please write the master password:')
            if USERINPUT == MASTER_PASSWORD:
                print('Please login to master user.')
                name = input('ID:')
                password = input('password:')
                if name == MASTERUSERNAME and password == MASTERUSERPASSWORD:
                    logging.warning('user status: logined to master mode.')
                    print('Changing mode to MASTER mode...')
                    master()


        else:
            print('The command you wrote do not exist.')
            time.sleep(0.3)
            print('Please try again. Or write "Help".')

def load_data():
    # ITEMSFORTXT = open('items.txt', 'r').readlines()
    # logging.info('val info:ITEMSFORTXT = ' + str(ITEMSFORTXT))
    items = "".join(open('itemsForPro.json').readlines())
    logging.info('val info:ITEMSFORPRO_RAW = ' + str(items))
    jsonItems = json.loads(items)
    logging.info('val info:ITEMSFORPRO = ' + str(jsonItems))
    return jsonItems

def print_items(items):
    print('------------------------------------------------')
    for k, v in items.items():
        print('| %s=%dP' % (k, v))
    print('------------------------------------------------')


def main():
    setup()

    items = load_data()

    user_File, user_Name, user_File_header, user_password, user_points = setup_login()
    logging.info('program status:changed to privted mode.')

    while True:
        USERIN = input('>local_kor:')
        if USERIN == 'buy' or USERIN == 'buy item':
            logging.info('user status:buying item.')
            print_items(items)

            while True:
                USERIN = input('please write the item you want to buy:')
                if USERIN in items:
                    break

                elif USERIN == 'ter':
                    print('going out...')
                    logging.warning('user status: user going out buy room...')
                    break

                else:
                    print('The item you wrote not exist.')
                    time.sleep(0.3)
                    print('Please try to write a different item.')
            if USERIN in items:
                logging.info('user status:buying item:' + str(USERIN))
                if user_points < items[str(USERIN)]:
                    print('You have not enogh points to buy "%s" item' % (str(USERIN)))
                    logging.info('user status: failed to buy item:%s.(not enogh points)' % (user_points))
                else:
                    logging.info('program status: Processing...')
                    print('구매중..')
                    user_File.close()
                    user_FileE = open(user_Name + '.csv', 'w')
                    user_FileE.write(user_password + '\n')
                    user_points = user_points - items[str(USERIN)]
                    user_FileE.write(str(user_points))
                    print('구매완료!')
                    logging.info('program status: Processing complete!')



        elif USERIN == 'logout':
            logging.warning('user status: logouting...')
            print('logouting...')
            del user_File, user_Name, user_File_header, user_password, user_points
            print('logout complete!')
            logging.info('user status: logouted.')
            user_File, user_Name, user_File_header, user_password, user_points = setup_login()


        # elif USERIN == 'return item' or USERIN == 'Return item' or USERIN == 'Return':
        #     RETURNITEM = input('What item do you want to return?')
        #     if RETURNITEM in items:
        #         userstatus = input('Do you really want to return %s?' % (RETURNITEM))
        #         if userstatus == 'y' or userstatus == 'yes':
        #             print('Returning item...')
        #             time.sleep(0.3)
        #             print('Returning points...')









if __name__ == '__main__':
    main()