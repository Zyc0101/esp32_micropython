import time

start_time = time.ticks_ms()  # 记录定时器启动时间

while True:
    current_time = time.ticks_ms()  # 获取当前时间
    
    elapsed_time = current_time - start_time  # 计算已经过去的时间（毫秒）
    
    print("已经过去的时间（毫秒）:", elapsed_time)
    
    time.sleep_ms(1000)  # 每秒更新一次时间，可以根据需求调整更新频率
