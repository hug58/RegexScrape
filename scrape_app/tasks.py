""" celery taks """
import re
from typing import Optional
import requests
from celery import shared_task

from django.core.cache import cache
from .models import RegexModel,PageExtract


@shared_task
def get_pages_and_process_with_regex(data:Optional[dict],_id:int) -> bool:
    """ Get page and get data from html using regex"""
    url:str = data['url_base']
    regexs:str = data['regex']
    page_html:str = ""
    result:dict= {}

    try:
        page_extract = PageExtract.objects.get(id = _id)
    except PageExtract.DoesNotExist:
        return False

    if cache.get(url, None) is None:
        print("No cache")
        response = requests.get(url, timeout=60)
        response.raise_for_status()
        page_html = response.text
        cache.set(url, page_html, 60*180)
    else:
        print("cache")
        page_html  = cache.get(url,None)


    for regex_id in regexs:
        try:
            regex = RegexModel.objects.get(id=regex_id)
        except  RegexModel.DoesNotExist:
            continue

        result[regex.name] = re.findall(regex.pattern, page_html)

    if page_extract.data is not None:
        for _,key in result.items():
            page_extract.data[key] = result[key]
    else:
        page_extract.data = result

    page_extract.save()
    return True
