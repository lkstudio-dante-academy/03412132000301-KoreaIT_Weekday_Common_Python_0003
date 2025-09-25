import os
import sys

from Training.Training_25.CManager_Member import CManager_Member

from Training.Training_29.CException_Duplicate import CException_Duplicate
from Training.Training_29.CException_Missing import CException_Missing

"""
Python 연습 문제 29
- 회원 관리 프로그램 제작하기 (+ 예외 처리 활용)
- 요구 사항은 연습 문제 18 번 참고
"""


# Training 29
def start(args):
	oManager = CManager_Member()
	
	while True:
		printMenu()
		nMenu = int(input("\n선택 : "))
		
		# 종료 일 경우
		if nMenu == MENU_EXIT:
			break
		
		try:
			# 회원 추가 일 경우
			if nMenu == MENU_ADD_MEMBER:
				addMember(oManager)
			
			# 회원 제거 일 경우
			elif nMenu == MENU_REMOVE_MEMBER:
				removeMember(oManager)
			
			# 회원 검색 일 경우
			elif nMenu == MENU_SEARCH_MEMBER:
				searchMember(oManager)
			
			# 모든 회원 출력 일 경우
			elif nMenu == MENU_PRINT_MEMBERS_ALL:
				printMembers_All(oManager)
				
		except Exception as oException:
			print(oException)
		
		print()
	
	print("프로그램을 종료합니다.")


# 메뉴
MENU_ADD_MEMBER = 1
MENU_REMOVE_MEMBER = 2
MENU_SEARCH_MEMBER = 3
MENU_PRINT_MEMBERS_ALL = 4
MENU_EXIT = 5

# 메뉴를 출력한다
def printMenu():
	print("=====> 메뉴 <=====")
	print("1. 회원 추가")
	print("2. 회원 제거")
	print("3. 회원 검색")
	print("4. 모든 회원 출력")
	print("5. 종료")


# 회원을 추가한다
def addMember(a_oManager):
	oName = input("이름 입력 : ")
	oPNumber = input("전화 번호 입력 : ")
	
	nResult = a_oManager.findMember(oName)
	
	# 회원이 존재 할 경우
	if nResult >= 0:
		raise CException_Duplicate(oName)
	
	a_oManager.addMember(oName, oPNumber)
	print(f"{oName} 을(를) 추가했습니다.")


# 회원을 제거한다
def removeMember(a_oManager):
	oName = input("이름 입력 : ")
	nResult = a_oManager.findMember(oName)
	
	# 회원이 없을 경우
	if nResult < 0:
		raise CException_Missing(oName)
	
	a_oManager.removeMember(oName)
	print(f"{oName} 을(를) 제거했습니다.")


# 회원을 검색한다
def searchMember(a_oManager):
	oName = input("이름 입력 : ")
	nResult = a_oManager.findMember(oName)
	
	# 회원이 없을 경우
	if nResult < 0:
		raise CException_Missing(oName)
	
	print("=====> 회원 정보 <=====")
	a_oManager.searchMember(oName)


# 모든 회원을 출력한다
def printMembers_All(a_oManager):
	print("=====> 모든 회원 정보 <=====")
	a_oManager.showMembers_All()
