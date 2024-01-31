# def 1
# def chek_soz(data:str, datas:str) -> bool:
#     if len(data) == len(datas):
#         return True
#     else:
#         return False


# def 2
# def chek_harf(data:str) -> int:
#     result = 0
#     for i in data:
#         if len(data) == 'a':
#             result +=1
#         elif len(data) == 'e':
#             result +=1
#         elif len(data) == 'o':
#             result +=1
#         elif len(data) == 'i':
#             result +=1
#         elif len(data) == 'u':
#             result +=1
#     return result

# def 3
# def chek_0(numbers):
#     num = '0'
#     result = 0
#     for i in numbers: 
#         if i in num:
#             result+=1
#     return result
# numbers = input('Raqamlarni kiriting ')
# results = chek_0(numbers)
# print(results)

# def 4
# def check_harflar(unli_soz, tekshiriladigan_soz):
#     unli_harflar = "a,e,i,o,u,A,E,I,O,U"  

#     unli_harflar_birinchi = set(harf for harf in unli_soz if harf in unli_harflar)

#     unli_mavjud = all(harf in unli_harflar_birinchi for harf in tekshiriladigan_soz)

#     return unli_mavjud

# birinchi_soz = "Salom"
# ikkinchi_soz = "Salom dunyo"
# natija = check_unli_harflar(birinchi_soz, ikkinchi_soz)
# print(f"Ikkinchi so'zda barcha birinchi so'zdagi unli harflar mavjud: {natija}")


"""echo "# 4-dars-uyga-vazifa" >> README.md
git init
git add README.md
git commit -m "first commit"
git branch -M main
git remote add origin https://github.com/ABDUMAJIDOVAA/4-dars-uyga-vazifa.git
git push -u origin main"""