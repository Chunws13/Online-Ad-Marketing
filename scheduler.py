import tkinter, time, datetime, sys, pandas, babel
from tktimepicker import constants, SpinTimePickerModern
from tkinter import filedialog, messagebox, ttk
from tkcalendar import DateEntry
from babel.numbers import *
import crawler, login_crawler, shopping

file = filedialog.askopenfilenames(initialdir="/", title="파일명 선택")
if not file:
    messagebox.showwarning("오류", "파일을 선택하세요")
    sys.exit()

window = tkinter.Tk()
window.title("Crawler")
window.geometry("300x300")

def clock_update():
    if option_box.get() == "기능 선택":
        messagebox.showwarning("오류", "기능을 선택하세요")
        return
    
    year, month, day = map(int, str(calendar.get_date()).split('-'))
    hour, minute = time_picker.hours(), time_picker.minutes()

    reserve_time = datetime.datetime(year, month, day, hour, minute, 0)
    remain_time = str(reserve_time - datetime.datetime.now()).split('.')[0].replace("days,", "일")

    now = datetime.datetime.now()

    current_time = time.strftime("%H:%M:%S")
    clock_label.config(text = "현재 시간 : {}".format(current_time))
    status_label.config(text = "{} 후 실행 예정".format(remain_time))

    request_list = pandas.read_excel(file[0])
    if day == now.day and hour == now.hour and minute == now.minute:
        option = option_box.get()
        status_label.config(text = "실행중")
        if option == "자사-로그인":
            login_crawler.login_crawler(request_list)
        
        elif option == "자사-비로그인":
            crawler.unlogin_crawler(request_list)
        
        else:
            shopping.shopping_crawl(request_list)

        return window.quit()

    window.after(1000, clock_update)

# 파일명 표기
file_name = tkinter.Label(window, text=file)
file_name.pack(padx=20)

# 크롤링 옵션
option_box = ttk.Combobox(window, text="선택", 
                          values=["네이버검색", "자사-로그인", "자사-비로그인"],
                          state="readonly",
                          width=200)
option_box.set("기능 선택")
option_box.pack(padx=20, pady=20)

# 현재 시간
clock_label = tkinter.Label(window, 
                            text="현재 시간 : {}".format(time.strftime("%H:%M:%S"))
                            )
clock_label.pack(pady=10)

# 진행 상황 표기 줄
status_label = tkinter.Label(window, text="시작 대기 중")
status_label.pack(padx=20, pady=10)

# 예약 일자
calendar = DateEntry(window, width=200)
calendar.pack(padx=20, pady=10)

# 예약 시간
time_picker = SpinTimePickerModern(window)
time_picker.addAll(constants.HOURS24)
time_picker.pack(padx=20, fill="both")

# 버튼 Method
button = tkinter.Button(window, command=clock_update, text="시작하기", width=200, height=10)
button.pack(padx=20, pady=25)
window.mainloop()
