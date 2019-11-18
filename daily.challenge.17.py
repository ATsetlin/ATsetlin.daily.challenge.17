year_born = input("What year were you born in?")

age = 2019 - int(year_born)

candle = (str(age)[-1])

candles = int(candle) * "i"

cake = ("         ___" + candles + "___\n" +
     """         |:H:a:p:p:y:|
       __|___________|__
      |^^^^^^^^^^^^^^^^^|
      |:B:i:r:t:h:d:a:y:|
      |                 |
      ~~~~~~~~~~~~~~~~~~~\n""")


if int(year_born) % 4 is 0:

	print(cake * 2) 

elif candle == 0;
  print("No cake for you!!")   

else:
	print(cake)