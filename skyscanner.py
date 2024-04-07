import time
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from datetime import datetime, timedelta

options = webdriver.SafariOptions()
options.add_argument("User-Agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.3.1 Safari/605.1.15"
                     "Cookie= _ga_XEEM7L2YCB=GS1.1.1712393122.3.0.1712393131.0.0.548885144; __Secure-anon_csrf_token=5b8c0bd7def0f93b36d599905ed5eb91; __Secure-anon_token=eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6ImM3ZGZlYjI2LTlmZjUtNDY4OC1iYjc3LWRiNTY2NWUyNjFkZSJ9.eyJhenAiOiIyNWM3MGZmZDAwN2JkOGQzODM3NyIsImh0dHBzOi8vc2t5c2Nhbm5lci5uZXQvbG9naW5UeXBlIjoiYW5vbnltb3VzIiwiaHR0cHM6Ly9za3lzY2FubmVyLm5ldC91dGlkIjoiOTI2NzIzYjAtOGM0MS00YWQzLWIyOGYtMmYxMDhjMzM5ZWE1IiwiaHR0cHM6Ly9za3lzY2FubmVyLm5ldC9jc3JmIjoiNWI4YzBiZDdkZWYwZjkzYjM2ZDU5OTkwNWVkNWViOTEiLCJodHRwczovL3NreXNjYW5uZXIubmV0L2p0aSI6ImQyODNhZDhjLWJlMmEtNDU0Zi1hY2E2LTE3NGNjOGM0ZjRiOSIsImlhdCI6MTcxMjM4NDg0NywiZXhwIjoxNzc1NDU2ODQ3LCJhdWQiOiJodHRwczovL2dhdGV3YXkuc2t5c2Nhbm5lci5uZXQvaWRlbnRpdHkiLCJpc3MiOiJodHRwczovL3d3dy5za3lzY2FubmVyLm5ldC9zdHRjL2lkZW50aXR5L2p3a3MvcHJvZC8ifQ.VDFKPAPOQgCgKAyhTdNwbuwRUhiEtjRg5pCilCStzNn_gneb5dkhvkpO_X1h_ywjZR8jAtt-Jqpmu8bBhWmknufcDoL8Eg2aFMnb78kKbfiYN2CH8OM3eVEwzGI9D8pBW9yqzH0ZqrYr7V7Dxs9bCX42U7HVPBhJ6YMaJ9ngyDyXrujJJIO3ET7yiLrfHnv4ZStoywJtoVgBkeTUaCjp60MLLRfTtdfL2MYzm4Gleskg5v1BQzEkS9HG8PGBfvZY1snjygcD0gD8iRB-7ZPlV7SzNyPq0thue0ZwbuSsgiaku9w8mxxbBY8g92Y0kiBKO0ZbpxLFJJgzKuL-p5McKw; __Secure-ska=23557873-7243-4f90-99aa-19bc8acf30a0; abgroup=98686762; avoid_banana_results=true; device_guid=23557873-7243-4f90-99aa-19bc8acf30a0; experiment_allocation_id=6d762eeb5fd9cd236c2de818f48a687f54fe76d18c132902440af305bb9a1411; scanner=currency:::TWD&legs:::TPE|2025-01-01|JP|JP|2025-01-05|TPE&tripType:::return&rtn:::true&preferDirects:::false&outboundAlts:::false&inboundAlts:::false&oym:::2501&oday:::01&wy:::0&iym:::2501&iday:::05&cabinclass:::Economy&adults:::5&adultsV2:::5&children:::0&childrenV2&infants:::0&from:::TPE&to:::JP; ssab=BD_Enable_Hops_for_some_market_V11:::a&BD_Enable_hide_tax_policy_V0:::b&BD_highlight_cheapest_rate_V4:::b&BD_longer_refresh_modal_V3:::b&Booking_Option_Card_MVP_V6:::b&HoPS_price_delta_HPA_desktop_V15:::b&LivePricingPoC2_V0:::a&MAT_grouping_v1_desktop_V2:::c&Node_Grpc_Client_Test_V5:::a&Partner_Differentiation_MVP_V10:::b&PersistSortingOptionsDesktop_V3:::a&SaveToListBookingPanelDesktop_V3:::b&Sonar_Rollout_V3:::a&ce_suggested_for_you_default_pill_web_V3:::a&ctr_model_experiment_V27:::b&desktop_move_best_icon_to_summary_text_V0:::b&dest_rec_route_summary_enabled_V1:::a&dmo_brand_incrementality_V0:::a&dmo_brand_incrementality_morocco_V0:::a&fdv_use_nebula_in_xsell_hotels_V1:::a&fps_mr_fqs_challenger_desktop__25i_desktop_V3:::a&hotel_ranking_ecpc_rerank_v1_desktop_web_V5:::a&hotelsBookingPanelVariants_V19:::d&mat_new_inline_ads_from_bumblebee_V3:::b&sam_split_test_014c57ebc3702dc0_V0:::b&sam_split_test_02fc902bf9cd8f44_V0:::a&sam_split_test_09c361dfa5404efc_V0:::b&sam_split_test_11d6ec1396e945ee_V0:::b&sam_split_test_1798bf3f3bad432c_V0:::b&sam_split_test_19f78c23af6d4b15_V0:::a&sam_split_test_311b78bdda9f4701_V0:::b&sam_split_test_311e9414eeab49e4_V0:::a&sam_split_test_3732aabcea3a4c30_V0:::b&sam_split_test_3eedcc979eae422e_V0:::a&sam_split_test_4052447056976bef_V0:::a&sam_split_test_419990afd1604da5_V0:::a&sam_split_test_478d34d3b5d24c5a_V0:::b&sam_split_test_53015babe8a645e4_V0:::a&sam_split_test_5c1ff4af28f54195_V0:::a&sam_split_test_6274b17c4594bd65_V0:::b&sam_split_test_653ff336209345b9_V0:::a&sam_split_test_6df29e1632ec47f3_V0:::a&sam_split_test_6e784daf796e4a8d_V0:::a&sam_split_test_868b4181_45b9_41_V0:::a&sam_split_test_884c8ffa650a4dc7_V0:::a&sam_split_test_8ba0b6c5c8adf97a_V0:::b&sam_split_test_8e14226cb83a465e_V0:::a&sam_split_test_91f25ab60a40424c_V0:::b&sam_split_test_94383f607cc7df8b_V0:::b&sam_split_test_9c2e5f203fe06a3f_V0:::b&sam_split_test_a0d0455407f48496_V0:::b&sam_split_test_a64a5e2887394182_V0:::b&sam_split_test_ab7444fa9ce54059_V0:::a&sam_split_test_b99079cf48c24d7c_V0:::a&sam_split_test_c586dc85c571e3bc_V0:::b&sam_split_test_c82c7bc93f04e3a1_V0:::b&sam_split_test_c8d4ebc13d7a48bc_V0:::a&sam_split_test_d1a0d40f0e034093_V0:::b&sam_split_test_dffea646638b43fc_V0:::a&sam_split_test_e38abc753ae34139_V0:::a&sam_split_test_e76da234f1514cb0_V0:::a&sam_split_test_eab0694968414955_V0:::a&sam_split_test_f074ee360dc8531a_V0:::a&sam_split_test_f17089679d72bb6d_V0:::a&sam_split_test_f95f38174e2273a6_V0:::b&sam_split_test_ffd06ce959eb44b9_V0:::b&self_transfer_messaging_V4:::a&terra_proxy_get_v2_suggested_airports_V1:::a; ssaboverrides=; ssculture=locale:::zh-TW&market:::TW&currency:::TWD; traveller_context=926723b0-8c41-4ad3-b28f-2f108c339ea5; _px3=c520685c847eab05db0610f8ed2d3f2156f93b9332fbb1c4d9788f26d68d8d58:PAd5c/c6KDY9XConJTpExz+BhxGYF9yvmiFLI2S0Gl4BuraMJW3hcq+sBnKi0qqiJktspcI9CIMpMNYWm5GRGQ==:1000:6xHkkCKlBPx/RCAsm//rkHFF2XhbT5pxxXD+LZ5ZaRghJyviI+E8ZrdK41RBSafHe65Ha6LlfMHhOzpoDtQ0b3YysA069h/WsEsDGDi/i6K+KRnesUxjmsbg17GkFiRRzvcZiVsTNwZuDrIUiP3BaAFVsfhmultnOz67Dnc1DivNMjpbQGN0RKzWo4srGr4EI6oFe+eO132JdV61Qj4YcCixxVldjJWvGxGSQabvOBM=; _pxhd=jdm2o2/TWaPZbDYx7D60iLGbQtFgMeUXoZ5ZSaytftG3N8-L2JXFx1qeTBbUNrvsKJ2vCW7viajSf75EuFpyyg==:/m2QwpBEaQu7bZyhE56uufrbjrD8nHXQnOhEEpUBsMW8XpvKlDRXYKaM-k1IDuoQyUSNeLXziOxIvR6C3--29W9/Dufn8rBf6-GTEv8gI/A=; _clsk=1opsfk1%7C1712391421181%7C3%7C0%7Ci.clarity.ms%2Fcollect; _uetsid=899a80c0f3ec11ee8f3ca5074819999f; _uetvid=899a7eb0f3ec11eea969b55c35650971; preferences=926723b08c414ad3b28f2f108c339ea5; __eoi=ID=56eaf3f98c371698:T=1712384848:RT=1712390774:S=AA-AfjaeW7V6EjCGlCZvFH0Ps1OL; __gads=ID=64b285a7a8f6af29:T=1712384848:RT=1712390774:S=ALNI_MZ7tfFOvmjukXmnimWmewVunDBpHw; __gpi=UID=00000de2c85fa4bf:T=1712384848:RT=1712390774:S=ALNI_MaKnaxfgHjmPJ1h10iSeVb8aLadpA; __gsas=ID=8e96d6ac601ea70c:T=1712390773:RT=1712390773:S=ALNI_MZYZtkpUY5y4MKADXQfxrJXJAWGpw; _clck=1y897ki%7C2%7Cfkp%7C0%7C1557; QSI_S_ZN_8fcHUNchqVNRM4S=v:0:0; _pxvid=bcc285bb-f3de-11ee-a648-9c116136e068; pxcts=c0140667-f3de-11ee-9477-564f0adb861d; _ga=GA1.1.23557873-7243-4f90-99aa-19bc8acf30a0.1712384848; _gcl_au=1.1.1892233777.1712384848; QSI_S_ZN_0VDsL2Wl8ZAlxlA=v:0:0")
driver = webdriver.Safari(options=options)

start_date = datetime(2025, 1, 2)
end_date = datetime(2025, 1, 7)

i = 1

while i < 6:
    url = f"https://www.skyscanner.com.tw/transport/flights/tpe/jp/{start_date.strftime("%Y%m%d")}/{end_date.strftime("%Y%m%d")}/?adultsv2=5"

    driver.get(url)
    time.sleep(5)

    places = driver.find_elements(By.CLASS_NAME,"PlaceCard_descriptionContainer__M2NjN")

    print(f"出發日：{start_date.strftime("%Y-%m-%d")}, 回程日：{end_date.strftime("%Y-%m-%d")} 資料如下")
    for place in places:
        print(place.text)

    print("-"*30)
    start_date += timedelta(days=1)
    end_date += timedelta(days=1)

    i += 1

html = driver.page_source







