import asyncio
from phang_download import pohang_download
from ulsan_download import ulsan_download
from gwongyang_download import gwaongyang_download
from incheon.incheon_E1_donwload import incheon_E1_dowonload
from incheon.incheon_HJIT_download import incheon_HJIT_download
from incheon.incheon_ICT_download import incheon_ICT_download
from incheon.incheon_SNCT_download import incheon_SNCT_download
from busan_download import busan_download
from get_req_urls import req_url_PH, query_date_PH
from get_req_urls import req_url_US
from get_req_urls import req_url_GW
import asyncio
import aioschedule
import time


async def get_forwarder():
    # 터미널 크롤링
    print("::: start schedule... :::")
    await asyncio.sleep(3)
    print("::: busan schedule... :::")
    busan_download()
    await asyncio.sleep(3)
    print("::: pohang schedule... :::")
    pohang_download(req_url_PH, query_date_PH)
    await asyncio.sleep(3)
    print("::: ulsan schedule... :::")
    ulsan_download(req_url_US)
    await asyncio.sleep(3)
    print("::: gwongyang schedule... :::")
    gwaongyang_download(req_url_GW)
    await asyncio.sleep(3)
    print("::: incheon E1 schedule... :::")
    incheon_E1_dowonload()
    await asyncio.sleep(3)
    print("::: incheon SNCT schedule... :::")
    incheon_SNCT_download()
    await asyncio.sleep(3)
    print("::: incheon HJIT schedule... :::")
    incheon_HJIT_download()
    await asyncio.sleep(3)
    print("::: incheon ICT schedule... :::")
    incheon_ICT_download()
    await asyncio.sleep(3)
    print("::: end schedule... :::")

aioschedule.every(10).minutes.do(get_forwarder)
loop = asyncio.get_event_loop()

while True:
    try:
        print('::: doing schedules... :::')
        print('-'*40)
        print('::: now time :::')
        print('-'*40)
        print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))
        print('-'*40)
        print('::: schedule pending time :::')
        print('-'*40)
        print(aioschedule.idle_seconds())
        print('-'*40)

        loop.run_until_complete(aioschedule.run_pending())
        time.sleep(1)

    except Exception as e:
        print(e)
        print("::: erorr!! now closing... :::")
        aioschedule.cancel_job(get_forwarder)
        loop.close()
