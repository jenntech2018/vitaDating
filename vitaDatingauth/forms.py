from django import forms
from vitaDatinguser.models import vitaDatinguser
MONTH =[(None, ""),
        ("1","January"),
        ("2","February"),
        ( "3","March"),
        ("4","April"),
        ( "5","May"),
        ( "6","June"),
        ( "7","July"),
        ( "8","August"),
        ( "9","September"),
        ("10","October"),
        ("11","November"),
        ("12","December")]
DAY = [(None, ""),
        ("1","1"),
        ("2","2"),
        ("3","3"),
        ("4","4"),
        ("5","5"),
        ("6","6"),
        ("7","7"),
        ("8","8"),
        ("9","9"),
        ("10","10"),
        ("11","11"),
        ("12","12"),
        ("13","13"),
        ("14","14"),
        ("15","15"),
        ("16","16"),
        ("17","17"),
        ("18","18"),
        ("19","19"),
        ("20","20"),
        ("21","21"),
        ("22","22"),
        ("23","23"),
        ("24","24"),
        ("25","25"),
        ("26","26"),
        ("37","37"),
        ("28","28"),
        ("29","29"),
        ("30","30"),
        ("31","31")]
YEAR = [(None, ""),
        ("2021",2021),
        ("2020",2020),
        ("2019",2019),
        ("2018",2018),
        ("2017",2017),
        ("2016",2016),
        ("2015",2015),
        ("2014",2014),
        ("2013",2013),
        ("2012",2012),
        ("2011",2011),
        ("2010",2010),
        ("2009",2009),
        ("2008",2008),
        ("2007",2007),
        ("2006",2006),
        ("2005",2005),
        ("2004",2004),
        ("2003",2003),
        ("2002",2002),
        ("2001",2001),
        ("2000",2000),
        ("1999",1999),
        ("1998",1998),
        ("1997",1997),
        ("1996",1996),
        ("1995",1995),
        ("1994",1994),
        ("1993",1993),
        ("1992",1992),
        ("1991",1991),
        ("1990",1990),
        ("1989",1989),
        ("1988",1988),
        ("1987",1987),
        ("1986",1986),
        ("1985",1985),
        ("1984",1984),
        ("1983",1983),
        ("1982",1982),
        ("1981",1981),
        ("1980",1980),
        ("1979",1979),
        ("1978",1978),
        ("1977",1977),
        ("1976",1976),
        ("1975",1975),
        ("1974",1974),
        ("1973",1973),
        ("1972",1972),
        ("1971",1971),
        ("1970",1970),
        ("1969",1969),
        ("1968",1968),
        ("1967",1967),
        ("1966",1966),
        ("1965",1965),
        ("1964",1964),
        ("1963",1963),
        ("1962",1962),
        ("1961",1961),
        ("1960",1960),
        ("1959",1959),
        ("1958",1958),
        ("1957",1957),
        ("1956",1956),
        ("1955",1955),
        ("1954",1954),
        ("1953",1953),
        ("1952",1952),
        ("1951",1951),
        ("1950",1950),
        ("1949",1949),
        ("1948",1948),
        ("1947",1947),
        ("1946",1946),
        ("1945",1945),
        ("1944",1944),
        ("1943",1943),
        ("1942",1942),
        ("1941",1941),
        ("1940",1940),
        ("1939",1939),
        ("1938",1938),
        ("1937",1937),
        ("1936",1936),
        ("1935",1935),
        ("1934",1934),
        ("1933",1933),
        ("1932",1932),
        ("1931",1931),
        ("1930",1930),
        ("1929",1929),
        ("1928",1928),
        ("1927",1927),
        ("1926",1926),
        ("1925",1925),
        ("1924",1924),
        ("1923",1923),
        ("1922",1922),
        ("1921",1921),
        ("1920",1920),
        ("1919",1919),
        ("1918",1918),
        ("1917",1917),
        ("1916",1916),
        ("1915",1915),
        ("1914",1914),
        ("1913",1913),
        ("1912",1912),
        ("1911",1911),
        ("1910",1910),
        ("1909",1909),
        ("1908",1908),
        ("1907",1907),
        ("1906",1906),
        ("1905",1905),
        ("1904",1904),
        ("1903",1903),
        ("1902",1902),
        ("1901",1901)]
class LoginForm(forms.Form):
    username = forms.CharField(max_length=100, widget=forms.TextInput(attrs={"id": 'email_or_username', "type":"text", "name":"email","placeholder":"Email or Username", "autofocus": "true", "class":"rounded-md h-12 border-gray-200 bg-gray-100 hover:bg-gray-200 mt-2 border-2 w-96"}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={"type":"password", 'id': "log-password","name":"password", "placeholder":"Password", "class":"rounded-md h-12 border-gray-200 bg-gray-100 hover:bg-gray-200 mt-2 border-2 w-96"}))


NONPROFIT_CHOICES = [
    ('HRC', 'www.humanrightswatch.com'),
    ('MoMA', 'www.moma.org'),
    ('UNICEF', 'www.unicef.org'),
    ('Doctors without borders', 'https://donate.doctorswithoutborders.org/medicalcare/donatenow'),
    ('Rotary International', 'www.rotary.org'),
    ('ACLU', 'www.aclu.org'),
]

class RegistrationForm(forms.Form):
    email = forms.EmailField(max_length=100, widget=forms.EmailInput(attrs={"type":"email", "name":"email", "id":"reg-email", "placeholder":"Email", "autofocus": "true", "class":"rounded-md h-12 border-gray-200 bg-gray-100 pl-3 hover:bg-gray-200 mt-2 border-2 w-96"}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={"type":"password", 'id': "reg-password", "name":"password", "placeholder":"Password", "class":"rounded-md h-12 border-gray-200 bg-gray-100 pl-3 hover:bg-gray-200 mt-2 border-2 w-96"}))
    day = forms.ChoiceField(choices=DAY, widget=forms.Select(attrs={"id": "day", "name": "day", "class": "w-28 h-12 bg-gray-100 hover:bg-gray-200 rounded"}))
    month = forms.ChoiceField(choices=MONTH, widget=forms.Select(attrs={"id": "month", "name": "month", "class": "w-28 h-12 bg-gray-100 hover:bg-gray-200 rounded"}))
    year = forms.ChoiceField(choices=YEAR, widget=forms.Select(attrs={"id": "year", "name": "year", "class": "w-28 h-12 bg-gray-100 hover:bg-gray-200 rounded"}))
    username = forms.CharField(required=False, max_length=32, widget=forms.TextInput(attrs={"name":"username", "placeholder":"Username", "class":"rounded-md inline h-12 border-gray-200 bg-gray-100 pl-3 hover:bg-gray-200 mt-2 border-2 w-96"}))
    display_name = forms.CharField(required=False, max_length=32, widget=forms.TextInput(attrs={"name":"display-name", "placeholder":"Display name", "class":"rounded-md inline h-12 border-gray-200 bg-gray-100 pl-3 hover:bg-gray-200 mt-2 border-2 w-96"}))
    profile_photo = forms.ImageField(required=False,widget=forms.ClearableFileInput(attrs={"id":"upload-pfp", "type":"file", "style":"font-size: 0; opacity: 0; top: 3.95rem; right: 13.425rem;", "class":"opacity-100 absolute w-8 h-8 cursor-pointer", "accept":"image/png,image/jpeg,image/jpg"}))
