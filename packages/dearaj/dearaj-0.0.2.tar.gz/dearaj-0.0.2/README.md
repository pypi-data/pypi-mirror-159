<div align="center">
  <img src="https://raw.githubusercontent.com/anzhi0708/dearAJ/main/img/logo.png" />
</div>

# dearAJ

Data analysis tool for Korean National Assembly

- [Installation](https://github.com/anzhi0708/dearAJ#install)
- [Usage](https://github.com/anzhi0708/dearAJ#usage)
  - [Conference](https://github.com/anzhi0708/dearAJ#conferences)
  - [Conferences](https://github.com/anzhi0708/dearAJ#conferences)
  - [MP](https://github.com/anzhi0708/dearAJ#mplist)
  - [MPList](https://github.com/anzhi0708/dearAJ#mplist)
  - [get_conferences_of](https://github.com/anzhi0708/dearAJ#get_conferences_of)(nth: int, save: bool, to: str, sleep: Union[float, int])
- [License](https://github.com/anzhi0708/dearAJ#license)

## Install

```bash
pip3 install dearaj
```
or
```bash
git clone https://github.com/anzhi0708/dearAJ
cd dearAJ
make install
```

## Usage

```python
from dearaj import *
```

### MPList

Collection of single `MP`s using data from [열린국회정보](https://open.assembly.go.kr/portal/assm/search/memberHistSchPage.do).

```python
>>> MPList(20)
MPList(male=267, female=53, total=320)
```
```python
>>> for mp in MPList(19):
...     if mp.name == '문재인':
...             print(mp)
...
MP(generation=19, name='문재인', party='민주통합당', committee=[], region='부산 사상구', gender='남', n='초선', how='지역구')
```

### Conferences

`Conferences(n)` is the collection of `n`th assembly's conferences.

```python
>>> Conferences(19)
<Conferences of 19th, total: 2605>
>>> Conferences(19)[0]
Conference(sami='1', angun_type=[], minutes='1', ct1='19', ct2='342', ct3='01', open_time='10:25', date='2016-05-19', hand_lang='0', mc='10', conf_title='제342회 국회(임시회) 제01차 본회의', comm_name='본회의', qvod=0)
```

`Conference`'s property `.pdf` is the PDF file raw bytes data. Use `open(output_file_path, "wb").write(conference.pdf)` to save PDF file.

### get_conferences_of

The crawler class. Use `get_conferences_of(nth, save=True)` to save JSON data to csv files.

## License

Copyright Anji Wong, 2022.

Distributed under the terms of the Apache 2.0 license.
