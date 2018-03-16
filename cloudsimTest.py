#coding:utf-8
#cloudsimTest.py


import time

from com.android.monkeyrunner import MonkeyRunner, MonkeyDevice
from com.android.monkeyrunner.easy import EasyMonkeyDevice
from com.android.monkeyrunner.easy import By

date = time.strftime('%Y%m%d%H%M%S')
#Connected devices
device = MonkeyRunner.waitForConnection()

takeSnapshotPath = 'C:\\Users\\Administrator\\Desktop\\test\\phone\\monkeyrunnerfile\\monkeyrunner_py\\takeSnapshot\\'+date
simtakeSnapshotPath = 'C:\\Users\\Administrator\\Desktop\\test\\phone\\monkeyrunnerfile\\monkeyrunner_py\\takeSnapshot\\cloudsim\\'+date
apkActivity = 'com.cootf.coolsim/.ui.activity.LoginActivity'
easy_device = EasyMonkeyDevice(device)  


def startApk():
	print("-------------startApk-------------")
	device.wake()
	#device.startActivity (component=apkActivity)
	device.touch(290,488,"DOWN_AND_UP")
	MonkeyRunner.sleep(8)
	device.wake()
	startResult=device.takeSnapshot()
	startResult.writeToFile(takeSnapshotPath+'startResult'+str(cont)+'.png','png')

def login():
	print("-------------login and cloudsim-------------")
	device.wake()
	#login user
	# device.touch(238,610,"DOWN_AND_UP")
	# device.type('liqingxia')
	# device.touch(175,693,"DOWN_AND_UP")
	# device.type('123456')
	# easy_device.touch(By.id('id/userNameLogin_btn'),MonkeyDevice.DOWN_AND_UP)
	device.touch(328,853,"DOWN_AND_UP")
	MonkeyRunner.sleep(60)
	device.wake()
	loginResult=device.takeSnapshot()
	loginResult.writeToFile(takeSnapshotPath+'loginResult'+str(cont)+'.png','png')

def cloudsimOnOff(i):
	print("-------------cloudsim On or Off-------------")
	device.wake()
	easy_device.touch(By.id('id/tb_cloudsim_on_off'),MonkeyDevice.DOWN_AND_UP)
	if i%2 == 0:
		MonkeyRunner.sleep(5)
	else:
		MonkeyRunner.sleep(60)
		cloudsimResult=device.takeSnapshot()
		cloudsimResult.writeToFile(simtakeSnapshotPath+'cloudsimResult'+str(i)+'.png','png')


def logoutUser():
	print("-------------logoutUser-------------")
	device.wake()
	#logout user
	# device.touch(659,114,"DOWN_AND_UP")
	easy_device.touch(By.id('id/tv_home_loginOrExit'),MonkeyDevice.DOWN_AND_UP)
	MonkeyRunner.sleep(3)
	device.wake()
	device.touch(580,765,"DOWN_AND_UP")
	endResult=device.takeSnapshot()
	endResult.writeToFile(takeSnapshotPath+'endResult'+str(cont)+'.png','png')

	#end Activity
def logoutApk():
	print("-------------logoutApk-------------")
	device.wake()
	device.press('KEYCODE_BACK','DOWN_AND_UP')
	MonkeyRunner.sleep(3)
	device.touch(582,762,"DOWN_AND_UP")
	device.wake()
	outResult=device.takeSnapshot()
	outResult.writeToFile(takeSnapshotPath+'outResult'+str(cont)+'.png','png')

def textAssert(idname,text):
	if easy_device.exists(By.id(idname)) == True:
		text = easy_device.getText(By.id(idname))
		if text.encode('utf-8') == text:
			print ("Assert pass")
		else:
			print ("Assert fail")
	else:
		print ("Assert fail")

def imageAssert(image,result):
	if image.sameAs(result,0.9):
		print("Assert pass")
	else:
		print("Assert fail")

if __name__ == "__main__":
	cont=100

	while cont>0:
		i = 10
		print("********************start",cont,"*********************")
		try:
			startApk()
			login()
			while i>0:
				cloudsimOnOff(i)
				i = i -1
			logoutUser()
			logoutApk()
			cont = cont - 1
		except BaseException:
			device.press('KEYCODE_HOME','DOWN_AND_UP')
			MonkeyRunner.sleep(3)

