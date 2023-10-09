import bs4
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
import re
from win11toast import toast


def web():
    my_url = 'https://warning.bmkg.go.id/'

    uClient = uReq(my_url)
    page_html = uClient.read()
    uClient.close()

    page_soup = soup(page_html, "html.parser")
    scrap = page_soup.findAll("div", {"class":"col-8"})
    page = scrap[0]

    return page

def magnitudo_gempa():
    magnitudo = web().div.select("li", {"img alt":"Magnitudo"})
    mag = magnitudo[0].text
    
    def angka_magnitude():
        ang_mag = r'[\d\W]'
        ang = re.findall(ang_mag, mag)
        an = ''.join(ang)

        return an

    def text_magnitude():
        hur_mag = r'[a-zA-Z]'
        hur = re.findall(hur_mag, mag)
        hu = ''.join(hur)

        return hu
    
    magni = angka_magnitude() + " " + text_magnitude()

    return magni

def waktu_gempa():
    waktu = web().div.select("h5")
    wkt = waktu[0].text

    return wkt

def lokasi_gempa():
    lokasi = web().div.select("p", {"class":"par"})
    lok = lokasi[0].text.split()
   
    def titik_gempa():
        ke = lok[1]
        pat = r'[a-zA-z]'
        ge = re.findall(pat, ke)
        tem = ''.join(ge)

        return tem

    def km_gempa():
        ke = lok[1]
        pola = r'[\d]'
        km = re.findall(pola, ke)
        kilo = ''.join(km)

        return kilo

    lok_pas = titik_gempa() + " " + km_gempa()
    lok[1] = lok_pas
    pos = " ".join(lok)

    return pos


toast("Update Gempa ", "Magnitudo : " + magnitudo_gempa() + '\n' + "Waktu: " + waktu_gempa() + '\n' + "Lokasi : " + lokasi_gempa())