#! /usr/bin/env python


#
# Liturgical calendar for Google Calendar
#
# Calculates the liturgical calendar formatted for Google Calendar.
#
# Joe Antognini
# Wed Nov 28 22:30:34 EST 2012
#

import datetime as dt
import calendar as cal
import sys

##
#
# Dates completed
#
# Movable feasts:
#
# Four Sundays of Advent
# Four Sundays of Lent
# Passion Sunday
# Palm Sunday
# Easter
# Low Sunday
# Pentecost
#
# Fixed feasts:
#
# Christmas
# Feast of the Immaculate Conception
#
##

nth = {
  1 : 'First',
  2 : 'Second',
  3 : 'Third',
  4 : 'Fourth',
  5 : 'Fifth',
  6 : 'Sixth',
  7 : 'Seventh',
  8 : 'Eighth',
  9 : 'Ninth',
  10 : 'Tenth',
  11 : 'Eleventh',
  12 : 'Twelfth',
  13 : 'Thirteenth',
  14 : 'Fourteenth',
  15 : 'Fifteenth',
  16 : 'Sixteenth',
  17 : 'Seventeenth',
  18 : 'Eighteenth',
  19 : 'Nineteenth',
  20 : 'Twentieth',
  21 : 'Twenty-first',
  22 : 'Twenty-second',
  23 : 'Twenty-third',
  24 : 'Twenty-fourth',
  25 : 'Twenty-fifth',
  26 : 'Twenty-sixth',
  27 : 'Twenty-seventh',
}

def easter_date(y):
  c = y / 100
  n = y - 19 * (y / 19)
  k = (c - 17) / 25
  i = c - c / 4 - (c - k) / 3 + 19 * n + 15
  i = i - 30 * (i / 30)
  i = i - (i / 28) * (1 - (i / 28) * (29 / (i + 1)) * ((21 - n) / 11))
  j = y + y / 4 + i + 2 - c + c / 4
  j = j - 7 * (j / 7)
  l = i - j
  m = 3 + (l + 40) / 44
  d = l + 28 - 31 * (m / 4)

  return dt.date(y, m, d)

# By default we compute the calendar from 1900 to 2100.  Otherwise, accept
# inputs to specify years.

if len(sys.argv) == 1:
  min_yr = 1900
  max_yr = 2100
elif len(sys.argv) == 2:
  min_yr = max_yr = int(sys.argv[1])
elif len(sys.argv) == 3:
  min_yr, max_yr = int(sys.argv[1:])

# Standard header
print "Subject,Start Date,Description"

for yr in range(min_yr, max_yr + 1):
  # Mark the season of Easter
  dates = []
  easter = easter_date(yr)
  dates.append(easter)
  print "Easter Sunday,%d/%d/%d,<a href=\'http://www.fisheaters.com/customseastertide1.html\'>Eastertide Overview</a><br><a href=\'http://www.fisheaters.com/customseastertide2.html\'>Easter Sunday</a>" % (easter.month, easter.day, easter.year)

  lowsunday = easter + dt.timedelta(7)
  dates.append(lowsunday)
  print "Low Sunday,%d/%d/%d,<a href=\'http://www.fisheaters.com/customseastertide4.html\'>Low Sunday</a>, also called Quasimodo Sunday" % (lowsunday.month, lowsunday.day, lowsunday.year)

  majorrogation = dt.date(yr, 4, 25)
  if majorrogation == easter or majorrogation == lowsunday:
    majorrogation += dt.timedelta(2)
  print "Major Rogation,%d/%d/%d,<a href=\'http://www.fisheaters.com/customseastertide3.html\'>Major Rogation</a>" % (majorrogation.month, majorrogation.day, majorrogation.year)

  easter2 = lowsunday + dt.timedelta(7)
  if easter2 not in dates:
    dates.append(easter2)
    print "Second Sunday after Easter,%d/%d/%d,<a href=\'http://www.fisheaters.com/customseastertide4.html\'>Eastertide Overview</a>" % (easter2.month, easter2.day, easter2.year)

  easter3 = easter2 + dt.timedelta(7)
  if easter3 not in dates:
    dates.append(easter3)
    print "Third Sunday after Easter,%d/%d/%d,<a href=\'http://www.fisheaters.com/customseastertide4.html\'>Eastertide Overview</a>" % (easter3.month, easter3.day, easter3.year)

  easter4 = easter3 + dt.timedelta(7)
  if easter4 not in dates:
    dates.append(easter4)
    print "Fourth Sunday after Easter,%d/%d/%d,<a href=\'http://www.fisheaters.com/customseastertide4.html\'>Eastertide Overview</a>" % (easter4.month, easter4.day, easter4.year)

  easter5 = easter4 + dt.timedelta(7)
  if easter5 not in dates:
    dates.append(easter5)
    print "Fifth Sunday after Easter,%d/%d/%d,<a href=\'http://www.fisheaters.com/customseastertide4.html\'>Eastertie Overview</a>" % (easter5.month, easter5.day, easter5.year)

  ascension = easter + dt.timedelta(39)
  dates.append(ascension)
  print "Ascension Thursday,%d/%d/%d,<a href=\'http://www.fisheaters.com/customseastertide6.html\'>Ascension Thursday</a>" % (ascension.month, ascension.day, ascension.year)

  minorrogationmon = ascension - dt.timedelta(3)
  dates.append(minorrogationmon)
  print "Minor Rogation,%d/%d/%d,<a href=\'http://www.fisheaters.com/customseastertide3.html\'>Minor Rogation</a>" % (minorrogationmon.month, minorrogationmon.day, minorrogationmon.year)

  minorrogationtue = minorrogationmon + dt.timedelta(1)
  dates.append(minorrogationtue)
  print "Minor Rogation,%d/%d/%d,<a href=\'http://www.fisheaters.com/customseastertide3.html\'>Minor Rogation</a>" % (minorrogationtue.month, minorrogationtue.day, minorrogationtue.year)

  minorrogationwed = minorrogationtue + dt.timedelta(1)
  dates.append(minorrogationwed)
  print "Minor Rogation,%d/%d/%d,<a href=\'http://www.fisheaters.com/customseastertide3.html\'>Minor Rogation</a>" % (minorrogationwed.month, minorrogationwed.day, minorrogationwed.year)

  sunpostasc = easter5 + dt.timedelta(7)
  dates.append(sunpostasc)
  print "Sunday after the Ascension,%d/%d/%d,<a href=\'http://www.fisheaters.com/customseastertide4.html\'>Sunday after the Ascension</a>" % (sunpostasc.month, sunpostasc.day, sunpostasc.year)

  pentecost = easter + dt.timedelta(49)
  dates.append(pentecost)
  print "Pentecost,%d/%d/%d,<a href=\'www.fisheaters.com/customseastertide7.html\'>Pentecost</a>, also called Whitsunday" % (pentecost.month, pentecost.day, pentecost.year)

  # Passiontide
  palmsunday = easter - dt.timedelta(7)
  dates.append(palmsunday)
  print "Palm Sunday,%d/%d/%d,<a href=\'http://www.fisheaters.com/customslent11.html\'>Palm Sunday</a>" % (palmsunday.month, palmsunday.day, palmsunday.year)

  passionsunday = palmsunday - dt.timedelta(7)
  dates.append(passionsunday)
  print "Passion Sunday,%d/%d/%d,<a href=\'http://www.fisheaters.com/customslent8.html\'>Passion Sunday</a>.  Passiontide begins." % (passionsunday.month, passionsunday.day, passionsunday.year)

  sevensorrows = passionsunday + dt.timedelta(5)
  dates.append(sevensorrows)
  print "The Seven Sorrows of Mary,%d/%d/%d,<a href=\'http://www.fisheaters.com/customslent8.html\'>The Seven Sorrows of Mary</a>" % (sevensorrows.month, sevensorrows.day, sevensorrows.year)

  spywednesday = palmsunday + dt.timedelta(3)
  dates.append(spywednesday)
  print "Spy Wednesday,%d/%d/%d,<a href=\'http://www.fisheaters.com/customslent11.html\'>Spy Wednesday</a>" % (spywednesday.month, spywednesday.day, spywednesday.year)

  maundythursday = spywednesday + dt.timedelta(1)
  dates.append(maundythursday)
  print "Maundy Thursday,%d/%d/%d,<a href=\'http://www.fisheaters.com/customslent11.html\'>Maundy Thursday</a>" % (maundythursday.month, maundythursday.day, maundythursday.year)

  goodfriday = maundythursday + dt.timedelta(1)
  dates.append(goodfriday)
  print "Good Friday,%d/%d/%d,<a href=\'http://www.fisheaters.com/customslent11.html\'>Good Friday</a>" % (goodfriday.month, goodfriday.day, goodfriday.year)

  holysaturday = goodfriday + dt.timedelta(1)
  dates.append(holysaturday)
  print "Holy Saturday,%d/%d/%d,<a href=\'http://www.fisheaters.com/customslent11.html\'>Holy Saturday</a>" % (holysaturday.month, holysaturday.day, holysaturday.year)

  # Lent
  lent1 = passionsunday - dt.timedelta(7 * 4)
  dates.append(lent1)
  print "First Sunday of Lent,%d/%d/%d,<a href=\'http://www.fisheaters.com/customslent1.html\'>Lent Overview</a>." % (lent1.month, lent1.day, lent1.year)

  lent2 = lent1 + dt.timedelta(7)
  dates.append(lent2)
  if lent2 == dt.date(yr, 3, 17):
    print "Second Sunday of Lent (St. Patrick),%d/%d/%d,<a href=\'http://www.fisheaters.com/customslent1.html\'>Lent Overview</a> <a href=\'http://www.fisheaters.com/customslent4.html\'>(St. Patrick)</a>." % (lent2.month, lent2.day, lent2.year)
  elif lent2 == dt.date(yr, 3, 19):
    print "Second Sunday of Lent (St. Joseph),%d/%d/%d,<a href=\'http://www.fisheaters.com/customslent1.html\'>Lent Overview</a> <a href=\'http://www.fisheaters.com/customslent5.html\'>(St. Joseph)</a>." % (lent2.month, lent2.day, lent2.year)
  else:
    print "Second Sunday of Lent,%d/%d/%d,<a href=\'http://www.fisheaters.com/customslent1.html\'>Lent Overview</a>." % (lent2.month, lent2.day, lent2.year)

  lent3 = lent2 + dt.timedelta(7)
  dates.append(lent3)
  if lent3 == dt.date(yr, 3, 17):
    print "Third Sunday of Lent (St. Patrick),%d/%d/%d,<a href=\'http://www.fisheaters.com/customslent1.html\'>Lent Overview</a> <a href=\'http://www.fisheaters.com/customslent4.html\'>(St. Patrick)</a>." % (lent3.month, lent3.day, lent3.year)
  elif lent3 == dt.date(yr, 3, 19):
    print "Third Sunday of Lent (St. Joseph),%d/%d/%d,<a href=\'http://www.fisheaters.com/customslent1.html\'>Lent Overview</a> <a href=\'http://www.fisheaters.com/customslent5.html\'>(St. Joseph)</a>." % (lent3.month, lent3.day, lent3.year)
  else:
    print "Third Sunday of Lent,%d/%d/%d,<a href=\'http://www.fisheaters.com/customslent1.html\'>Lent Overview</a>." % (lent3.month, lent3.day, lent3.year)

  laetare = lent3 + dt.timedelta(7)
  dates.append(laetare)
  if lent3 == dt.date(yr, 3, 17):
    print "Laetare Sunday (St. Patrick),%d/%d/%d,<a href=\'http://www.fisheaters.com/customslent1.html\'>Lent Overview</a> <a href=\'http://www.fisheaters.com/customslent4.html\'>(St. Patrick)</a>." % (laetare.month, laetare.day, laetare.year)
  elif lent3 == dt.date(yr, 3, 19):
    print "Laetare Sunday (St. Joseph),%d/%d/%d,<a href=\'http://www.fisheaters.com/customslent1.html\'>Lent Overview</a> <a href=\'http://www.fisheaters.com/customslent5.html\'>(St. Joseph)</a>." % (laetare.month, laetare.day, laetare.year)
  else:
    print "Laetare Sunday,%d/%d/%d,<a href=\'http://www.fisheaters.com/customslent7.html\'>Laetare Sunday</a>." % (laetare.month, laetare.day, laetare.year)

  ashwednesday = lent1 - dt.timedelta(4)
  dates.append(ashwednesday)
  print "Ash Wednesday,%d/%d/%d,<a href=\'http://www.fisheaters.com/customslent2.html\'>Ash Wednesday</a>." % (ashwednesday.month, ashwednesday.day, ashwednesday.year)

  # Christmas
  christmas = dt.date(yr-1, 12, 25)
  dates.append(christmas)
  print "Christmas,%d/%d/%d,<a href=\'http://www.fisheaters.com/customschristmas2.html/'>Christmas Day</a><br><a href=\'http://www.fisheaters.com/customschristmas1.html\'>Christmastide Overview</a>" % (christmas.month, christmas.day, christmas.year)

  # Before we embark on Advent, we have to do the Feast of the Immaculate
  # Conception in case it conflicts with a Sunday of Advent.
  immaculate = dt.date(yr-1, 12, 8)
  dates.append(immaculate)
  print "Feast of the Immaculate Conception,%d/%d/%d,<a href=\'http://www.fisheaters.com/customsadvent5.html\'>Feast of the Immaculate Conception</a>" % (immaculate.month, immaculate.day, immaculate.year)

  # Now Advent.
  if christmas.weekday() != 6:
    advent4 = christmas - dt.timedelta(christmas.weekday() + 1)
  else:
    advent4 = christmas + dt.timedelta(-7)
  dates.append(advent4)
  print "Fourth Sunday of Advent,%d/%d/%d,<a href=\'http://www.fisheaters.com/customsadvent1.html\'>Advent Overview</a>" % (advent4.month, advent4.day, advent4.year)

  advent3 = advent4 - dt.timedelta(7)
  dates.append(advent3)
  if advent3 == dt.date(yr-1, 12, 12):
    dates.append(advent3)
    print "Gaudete Sunday (Feast of Our Lady of Guadalupe),%d/%d/%d,<a href=\'http://www.fisheaters.com/customsadvent1.html\'>Advent Overview</a> <a href=\'http://www.fisheaters.com/customsadvent6.html\'>(Our Lady of Guadalupe)</a>" % (advent3.month, advent3.day, advent3.year)
  elif advent3 == dt.date(yr-1, 12, 13):
    dates.append(advent3)
    print "Gaudete Sunday (St. Lucy),%d/%d/%d,<a href=\'http://www.fisheaters.com/customsadvent1.html\'>Advent Overview</a> <a href=\'http://www.fisheaters.com/customsadvent6a.html\'>(St. Lucy)</a>" % (advent3.month, advent3.day, advent3.year)
  else:
    print "Gaudete Sunday,%d/%d/%d,<a href=\'http://www.fisheaters.com/customsadvent1.html\'>Advent Overview</a>" % (advent3.month, advent3.day, advent3.year)

  advent2 = advent3 - dt.timedelta(7)
  if advent2 not in dates:
    if advent2 == dt.date(yr-1, 12, 4):
      dates.append(advent2)
      print "Second Sunday of Advent (St. Barbara),%d/%d/%d,<a href=\'http://www.fisheaters.com/customsadvent1.html\'>Advent Overview</a> <a href=\'http://www.fisheaters.com/customsadvent2a.html\'>(St. Barbara)</a>" % (advent2.month, advent2.day, advent2.year)
    elif advent2 == dt.date(yr-1, 12, 6):
      dates.append(advent2)
      print "Second Sunday of Advent (St. Nicholas),%d/%d/%d,<a href=\'http://www.fisheaters.com/customsadvent1.html\'>Advent Overview</a> <a href=\'http://www.fisheaters.com/customsadvent3.html\'>(St. Nicholas)</a>" % (advent2.month, advent2.day, advent2.year)
    else:
      dates.append(advent2)
      print "Second Sunday of Advent,%d/%d/%d,<a href=\'http://www.fisheaters.com/customsadvent1.html\'>Advent Overview</a>" % (advent2.month, advent2.day, advent2.year)

  advent1 = advent2 - dt.timedelta(7)
  dates.append(advent1)
  print "Advent Sunday,%d/%d/%d,<a href=\'http://www.fisheaters.com/customsadvent1.html\'>Advent Overview</a>" % (advent1.month, advent1.day, advent1.year)

  advent_ember_wednesday = advent3 + dt.timedelta(3)
  dates.append(advent_ember_wednesday)
  print "Advent Embertide,%d/%d/%d,<a href=\'http://www.fisheaters.com/customsadvent11.html\'>Advent Embertide</a>" % (advent_ember_wednesday.month, advent_ember_wednesday.day, advent_ember_wednesday.year)

  advent_ember_friday = advent_ember_wednesday + dt.timedelta(2)
  dates.append(advent_ember_friday)
  print "Advent Embertide,%d/%d/%d,<a href=\'http://www.fisheaters.com/customsadvent11.html\'>Advent Embertide</a>" % (advent_ember_friday.month, advent_ember_friday.day, advent_ember_friday.year)

  advent_ember_saturday = advent_ember_friday + dt.timedelta(1)
  dates.append(advent_ember_saturday)
  print "Advent Embertide,%d/%d/%d,<a href=\'http://www.fisheaters.com/customsadvent11.html\'>Advent Embertide</a>" % (advent_ember_saturday.month, advent_ember_saturday.day, advent_ember_saturday.year)

  # Christmastide
  christmaseve = christmas - dt.timedelta(1)
  if christmaseve not in dates:
    dates.append(christmaseve)
    print "Christmas Eve,%d/%d/%d,<a href=\'http://www.fisheaters.com/customschristmas2.html\'>Christmas Eve</a>" % (christmaseve.month, christmaseve.day, christmaseve.year)

  if 6 - christmas.weekday() != 0:
    sundayinxmas = christmas + dt.timedelta(6 - christmas.weekday())
  else:
    sundayinxmas = christmas + dt.timedelta(7)
  dates.append(sundayinxmas)
  print "Sunday within the Octave of the Nativity,%d/%d/%d,<a href=\'http://www.fisheaters.com/customschristmas1.html\'>Christmastide Overview</a>" % (sundayinxmas.month, sundayinxmas.day, sundayinxmas.year)

  ststephen = dt.date(yr-1, 12, 26)
  if ststephen not in dates:
    dates.append(ststephen)
    print "St. Stephen,%d/%d/%d,<a href=\'http://www.fisheaters.com/customschristmas3.html\'>St. Stephen</a>" % (ststephen.month, ststephen.day, ststephen.year)

  stjohnevang = dt.date(yr-1, 12, 27)
  if stjohnevang not in dates:
    dates.append(stjohnevang)
    print "St. John the Evangelist,%d/%d/%d,<a href=\'http://www.fisheaters.com/customschristmas4.html\'>St. John the Evangelist</a>" % (stjohnevang.month, stjohnevang.day, stjohnevang.year)

  childermas = dt.date(yr-1, 12, 28)
  if childermas not in dates:
    dates.append(childermas)
    print "Childermas,%d/%d/%d,<a href=\'http://www.fisheaters.com/customschristmas5.html\'>Childermas</a>" % (childermas.month, childermas.day, childermas.year)

  sttbecket = dt.date(yr-1, 12, 29)
  if sttbecket not in dates:
    dates.append(sttbecket)
    print "St. Thomas Becket,%d/%d/%d,<a href=\'http://www.fisheaters.com/customschristmasx.html\'>St. Thomas Becket</a>" % (sttbecket.month, sttbecket.day, sttbecket.year)

  stsylvester = dt.date(yr-1, 12, 31)
  if stsylvester not in dates:
    dates.append(stsylvester)
    print "St. Sylvester,%d/%d/%d,<a href=\'http://www.fisheaters.com/customschristmas6.html\'>St. Sylvester</a>" % (stsylvester.month, stsylvester.day, stsylvester.year)

  circumcision = dt.date(yr, 1, 1)
  dates.append(circumcision)
  print "Feast of the Circumcision,%d/%d/%d,<a href=\'http://www.fisheaters.com/customschristmas7.html\'>Feast of the Circumcision</a>" % (circumcision.month, circumcision.day, circumcision.year)

  epiphany = dt.date(yr, 1, 6)
  dates.append(epiphany)
  print "Epiphany,%d/%d/%d,<a href=\'http://www.fisheaters.com/customschristmas8.html\'>Epiphany</a>" % (epiphany.month, epiphany.day, epiphany.year)

  holyname = dt.date(yr, 1, 1) + dt.timedelta(6 - dt.date(yr, 1, 1).weekday())
  if (holyname == dt.date(yr, 1, 1) or holyname == dt.date(yr, 1, 2) or 
    holyname == dt.date(yr, 1, 6)):
    holyname = dt.date(yr, 1, 2)
  dates.append(holyname)
  print "Feast of the Holy Name,%d/%d/%d,<a href=\'http://www.fisheaters.com/customschristmas7a.html\'>Feast of the Holy Name</a>" % (holyname.month, holyname.day, holyname.year)

  twelfthnight = dt.date(yr, 1, 5)
  if twelfthnight not in dates:
    dates.append(twelfthnight)
    print "Twelfth Night,%d/%d/%d,<a href=\'http://www.fisheaters.com/epiphanyeve.html\'>Twelfth Night</a>" % (twelfthnight.month, twelfthnight.day, twelfthnight.year)

  if 6 - epiphany.weekday() != 0:
    holyfamily = epiphany + dt.timedelta(6 - epiphany.weekday())
  else:
    holyfamily = epiphany + dt.timedelta(7)
  dates.append(holyfamily)
  print "Feast of the Holy Family,%d/%d/%d,<a href=\'http://www.fisheaters.com/customstimeafterepiphany1a.html\'>Feast of the Holy Family</a>" % (holyfamily.month, holyfamily.day, holyfamily.year)

  baptism = dt.date(yr, 1, 13)
  if baptism not in dates:
    dates.append(baptism)
    print "The Baptism of Our Lord,%d/%d/%d,<a href=\'http://www.fisheaters.com/baptism3.html\'>The Baptism of Our Lord</a>" % (baptism.month, baptism.day, baptism.year)

  candlemas = dt.date(yr, 2, 2)
  dates.append(candlemas)
  print "Candlemas,%d/%d/%d,<a href=\'http://www.fisheaters.com/customstimeafterepiphany3.html\'>Candlemas</a>" % (candlemas.month, candlemas.day, candlemas.year)

  # Septuagesima
  quinquagesima = lent1 + dt.timedelta(-7)
  if quinquagesima not in dates:
    dates.append(quinquagesima)
    print "Quinquagesima,%d/%d/%d,<a href=\'http://www.fisheaters.com/customsseptuagesima1.html\'>Septuagesima Overview</a>" % (quinquagesima.month, quinquagesima.day, quinquagesima.year)

  sexagesima = quinquagesima + dt.timedelta(-7)
  if sexagesima not in dates:
    dates.append(sexagesima)
    print "Sexagesima,%d/%d/%d,<a href=\'http://www.fisheaters.com/customsseptuagesima1.html\'>Septuagesima Overview</a>" % (sexagesima.month, sexagesima.day, sexagesima.year)

  septuagesima = sexagesima + dt.timedelta(-7)
  if septuagesima not in dates:
    dates.append(septuagesima)
    print "Septuagesima,%d/%d/%d,<a href=\'http://www.fisheaters.com/septuagesima.html\'>Septuagesima</a>" % (septuagesima.month, septuagesima.day, septuagesima.year)

  shrovetide = quinquagesima + dt.timedelta(2)
  dates.append(shrovetide)
  print "Mardi Gras (Shrovetide),%d/%d/%d,<a href=\'http://www.fisheaters.com/septuagesima.html\'>Shrovetide</a>" % (shrovetide.month, shrovetide.day, shrovetide.year)

  lent_ember_wed = lent1 + dt.timedelta(3)
  dates.append(lent_ember_wed)
  print "Lenten Embertide,%d/%d/%d,<a href=\'http://www.fisheaters.com/customslent3.html\'>Lenten Embertide</a>." % (lent_ember_wed.month, lent_ember_wed.day, lent_ember_wed.year)

  lent_ember_fri = lent_ember_wed + dt.timedelta(2)
  dates.append(lent_ember_fri)
  print "Lenten Embertide,%d/%d/%d,<a href=\'http://www.fisheaters.com/customslent3.html\'>Lenten Embertide</a>." % (lent_ember_fri.month, lent_ember_fri.day, lent_ember_fri.year)

  lent_ember_sat = lent_ember_fri + dt.timedelta(1)
  dates.append(lent_ember_sat)
  print "Lenten Embertide,%d/%d/%d,<a href=\'http://www.fisheaters.com/customslent3.html\'>Lenten Embertide</a>." % (lent_ember_sat.month, lent_ember_sat.day, lent_ember_sat.year)

  # Time after Pentecost
  whitemberwed = pentecost + dt.timedelta(3)
  dates.append(whitemberwed)
  print "Whit Embertide,%d/%d/%d,<a href=\'http://www.fisheaters.com/customseastertide8.html\'>Whit Embertide</a>." % (whitemberwed.month, whitemberwed.day, whitemberwed.year)

  whitemberfri = whitemberwed + dt.timedelta(2)
  dates.append(whitemberfri)
  print "Whit Embertide,%d/%d/%d,<a href=\'http://www.fisheaters.com/customseastertide8.html\'>Whit Embertide</a>." % (whitemberfri.month, whitemberfri.day, whitemberfri.year)

  whitembersat = whitemberfri + dt.timedelta(1)
  dates.append(whitembersat)
  print "Whit Embertide,%d/%d/%d,<a href=\'http://www.fisheaters.com/customseastertide8.html\'>Whit Embertide</a>." % (whitembersat.month, whitembersat.day, whitembersat.year)

  trinitysunday = pentecost + dt.timedelta(7)
  dates.append(trinitysunday)
  print "Trinity Sunday,%d/%d/%d,<a href=\'http://www.fisheaters.com/customseastertide9.html\'>Trinity Sunday</a>." % (trinitysunday.month, trinitysunday.day, trinitysunday.year)

  corpuschristi = trinitysunday + dt.timedelta(4)
  dates.append(corpuschristi)
  print "Corpus Christi,%d/%d/%d,<a href=\'http://www.fisheaters.com/customstimeafterpentecost2.html\'>Corpus Christi</a>." % (corpuschristi.month, corpuschristi.day, corpuschristi.year)

  sacredheart = corpuschristi + dt.timedelta(8)
  dates.append(sacredheart)
  print "Feast of the Sacred Heart,%d/%d/%d,<a href=\'http://www.fisheaters.com/customstmeafterpentecost4.html\'>Feast of the Sacred Heart</a>." % (sacredheart.month, sacredheart.day, sacredheart.year)

  sspeterpaul = dt.date(yr, 6, 29)
  dates.append(sspeterpaul)
  print "Saints Peter and Paul,%d/%d/%d,Saints Peter and Paul" % (sspeterpaul.month, sspeterpaul.day, sspeterpaul.year)

  preciousblood = dt.date(yr, 7, 1)
  dates.append(preciousblood)
  print "Most Precious Blood,%d/%d/%d,Most Precious Blood" % (preciousblood.month, preciousblood.day, preciousblood.year)

  visitation = dt.date(yr, 7, 2)
  if visitation not in dates:
    dates.append(visitation)
    print "Feast of the Visitation,%d/%d/%d,<a href=\'http://www.fisheaters.com/visitation.html\'>Feast of the Visitation</a>." % (visitation.month, visitation.day, visitation.year)

  roodmas = dt.date(yr, 9, 14)
  dates.append(roodmas)
  print "Roodmas,%d/%d/%d,<a href=\'http://www.fisheaters.com/customstimeafterpentecost7.html\'>Roodmas</a>." % (roodmas.month, roodmas.day, roodmas.year)

  firstsunsept = dt.date(yr, 9, 1) + dt.timedelta(6 - dt.date(yr, 9, 1).weekday())
  michaelmasemberwed = firstsunsept + dt.timedelta(17)
  dates.append(michaelmasemberwed)
  print "Michaelas Embertide,%d/%d/%d,<a href=\'http://www.fisheaters.com/customstimeafterpentecost8.html\'>Michaelmas Embertide</a>." % (michaelmasemberwed.month, michaelmasemberwed.day, michaelmasemberwed.year)

  michaelmasemberfri = michaelmasemberwed + dt.timedelta(2)
  dates.append(michaelmasemberfri)
  print "Michaelas Embertide,%d/%d/%d,<a href=\'http://www.fisheaters.com/customstimeafterpentecost8.html\'>Michaelmas Embertide</a>." % (michaelmasemberfri.month, michaelmasemberfri.day, michaelmasemberfri.year)

  michaelmasembersat = michaelmasemberfri + dt.timedelta(1)
  dates.append(michaelmasembersat)
  print "Michaelas Embertide,%d/%d/%d,<a href=\'http://www.fisheaters.com/customstimeafterpentecost8.html\'>Michaelmas Embertide</a>." % (michaelmasembersat.month, michaelmasembersat.day, michaelmasembersat.year)

  christking = dt.date(yr, 11, 1) - dt.timedelta(1 + dt.date(yr, 11, 1).weekday())
  dates.append(christking)
  print "Feast of Christ the King,%d/%d/%d,<a href=\'http://www.fisheaters.com/customstimeafterpentecost11.html\'>Michaelmas Embertide</a>." % (christking.month, christking.day, christking.year)

  nextadvent4 = dt.date(yr, 12, 25) -dt.timedelta(dt.date(yr, 12, 25).weekday() + 1)
  nextadvent1 = nextadvent4 - dt.timedelta(21)
  lastsunday = nextadvent1 - dt.timedelta(7)
  dates.append(lastsunday)
  print "Last Sunday after Pentecost,%d/%d/%d,<a href=\'http://www.fisheaters.com/customstimeafterpentecost13.html\'>Last Sunday after Pentecost</a>" % (lastsunday.month, lastsunday.day, lastsunday.year)

  # Fill in second class feasts
  stjoseph = dt.date(yr, 3, 19)
  if stjoseph not in dates:
    dates.append(stjoseph)
    print "St. Joseph,%d/%d/%d,<a href=\'http://www.fisheaters.com/customslent5.html\'>St. Joseph</a>" % (stjoseph.month, stjoseph.day, stjoseph.year)

  ladyday = dt.date(yr, 3, 25)
  if ladyday not in dates:
    dates.append(ladyday)
    print "Lady Day,%d/%d/%d,<a href=\'http://www.fisheaters.com/customslent6.html\'>Lady Day</a>" % (ladyday.month, ladyday.day, ladyday.year)
    
  queenship = dt.date(yr, 5, 31)
  if queenship not in dates:
    dates.append(queenship)
    print "The Queenship of Mary,%d/%d/%d,<a href=\'http://www.fisheaters.com/queenshipofmary.html\'>The Queenship of Mary</a>" % (queenship.month, queenship.day, queenship.year)

  stjohn = dt.date(yr, 6, 24)
  if stjohn not in dates:
    dates.append(stjohn)
    print "St. John's Day,%d/%d/%d,<a href=\'http://www.fisheaters.com/customstimeafterpentecost3.html\'>St. John's Day</a>" % (stjohn.month, stjohn.day, stjohn.year)

  stjames = dt.date(yr, 7, 25)
  if stjames not in dates:
    dates.append(stjames)
    print "St. James the Greater,%d/%d/%d,<a href=\'http://www.fisheaters.com/customstimeafterpentecost4x.html\'>St. James the Greater</a>" % (stjames.month, stjames.day, stjames.year)

  transfiguration = dt.date(yr, 8, 6)
  if transfiguration not in dates:
    dates.append(transfiguration)
    print "The Transfiguration,%d/%d/%d,<a href=\'http://www.fisheaters.com/customstimeafterpentecost5.html\'>The Transfiguration</a>" % (transfiguration.month, transfiguration.day, transfiguration.year)

  stlawrence = dt.date(yr, 8, 10)
  if stlawrence not in dates:
    dates.append(stlawrence)
    print "St. Lawrence,%d/%d/%d,<a href=\'http://www.fisheaters.com/stlawrence.html\'>St. Lawrence</a>" % (stlawrence.month, stlawrence.day, stlawrence.year)

  marymass = dt.date(yr, 8, 15)
  if marymass not in dates:
    dates.append(marymass)
    print "Marymass,%d/%d/%d,<a href=\'http://www.fisheaters.com/customstimeafterpentecost6.html\'>Marymass</a>" % (marymass.month, marymass.day, marymass.year)

  stbartholomew = dt.date(yr, 8, 24)
  if stbartholomew not in dates:
    dates.append(stbartholomew)
    print "St. Bartholomew,%d/%d/%d,St. Bartholomew" % (stbartholomew.month, stbartholomew.day, stbartholomew.year)

  nativitymary = dt.date(yr, 9, 8)
  if nativitymary not in dates:
    dates.append(nativitymary)
    print "Nativity of Mary,%d/%d/%d,<a href=\'http://www.fisheaters.com/customstimeafterpentecost6a.html\'>Nativity of Mary</a>" % (nativitymary.month, nativitymary.day, nativitymary.year)

  michaelmas = dt.date(yr, 9, 29)
  if michaelmas not in dates:
    dates.append(michaelmas)
    print "Michaelmas,%d/%d/%d,<a href=\'http://www.fisheaters.com/customstimeafterpentecost10.html\'>Michaelmas</a>" % (michaelmas.month, michaelmas.day, michaelmas.year)

  hallowmas = dt.date(yr, 11, 1)
  if hallowmas not in dates:
    dates.append(hallowmas)
    print "Hallowmas,%d/%d/%d,<a href=\'http://www.fisheaters.com/customstimeafterpentecost12.html\'>Hallowmas</a>" % (hallowmas.month, hallowmas.day, hallowmas.year)

  soulsday = dt.date(yr, 11, 2)
  if soulsday not in dates:
    dates.append(soulsday)
    print "All Souls' Day,%d/%d/%d,<a href=\'http://www.fisheaters.com/customstimeafterpentecost12ac.html\'>All Souls' Day</a>" % (soulsday.month, soulsday.day, soulsday.year)

  # Sundays after Epiphany
  i = 0
  if 6 - epiphany.weekday() != 0:
    sunday = epiphany + dt.timedelta(6 - epiphany.weekday())
  else:
    sunday = epiphany + dt.timedelta(7)
  while sunday < septuagesima:
    if sunday not in dates:
      if sunday == dt.date(yr, 1, 17):
        dates.append(sunday)
        print "%s Sunday after Epiphany (St. Anthony of the Desert),%d/%d/%d,<a href=\'http://www.fisheaters.com/customstimeafterepiphany1.html\'>Time after Epiphany Overview</a> (St. Anthony of the Desert)" % (nth[i], sunday.month, sunday.day, sunday.year)
      elif sunday == dt.date(yr, 1, 21):
        dates.append(sunday)
        print "%s Sunday after Epiphany (St. Agnes),%d/%d/%d,<a href=\'http://www.fisheaters.com/customstimeafterepiphany1.html\'>Time after Epiphany Overview</a> <a href=\'http://www.fisheaters.com/customstimeafterepiphany2.html\'>(St. Agnes)</a>" % (nth[i], sunday.month, sunday.day, sunday.year)
      elif sunday == dt.date(yr, 2, 1):
        dates.append(sunday)
        print "%s Sunday after Epiphany (St. Brigid),%d/%d/%d,<a href=\'http://www.fisheaters.com/customstimeafterepiphany1.html\'>Time after Epiphany Overview</a> <a href=\'http://www.fisheaters.com/customstimeafterepiphany2a.html\'>(St. Brigid)</a>" % (nth[i], sunday.month, sunday.day, sunday.year)
      elif sunday == dt.date(yr, 2, 3):
        dates.append(sunday)
        print "%s Sunday after Epiphany (St. Blaise),%d/%d/%d,<a href=\'http://www.fisheaters.com/customstimeafterepiphany1.html\'>Time after Epiphany Overview</a> <a href=\'http://www.fisheaters.com/customstimeafterepiphany4.html\'>(St. Blaise)</a>" % (nth[i], sunday.month, sunday.day, sunday.year)
      elif sunday == dt.date(yr, 2, 14):
        dates.append(sunday)
        print "%s Sunday after Epiphany (St. Valentine),%d/%d/%d,<a href=\'http://www.fisheaters.com/customstimeafterepiphany1.html\'>Time after Epiphany Overview</a> <a href=\'http://www.fisheaters.com/customstimeafterepiphany5.html\'>(St.  Valentine)</a>" % (nth[i], sunday.month, sunday.day, sunday.year)
      else:
        dates.append(sunday)
        print "%s Sunday after Epiphany,%d/%d/%d,<a href=\'http://www.fisheaters.com/customstimeafterepiphany1.html\'>%s Sunday after Epiphany</a>" % (nth[i], sunday.month, sunday.day, sunday.year, nth[i])
    i += 1
    sunday += dt.timedelta(7)

  # Sundays after Pentecost
  i = 1
  sunday = pentecost + dt.timedelta(7)
  while sunday < lastsunday:
    if sunday not in dates:
      dates.append(sunday)
      if sunday == dt.date(yr, 6, 13):
        print "%s Sunday after Pentecost (St. Anthony of Padua),%d/%d/%d,<a href=\'http://www.fisheaters.com/customstimeafterpentecost1.html\'>Time after Pentecost Overview</a> <a href=\'http://www.fisheaters.com/customstimeafterpentecoststa.html\'>(St. Anthony of Padua)</a>" % (nth[i], sunday.month, sunday.day, sunday.year, nth[i])
      elif abs(sunday - dt.date(yr, 6, 29)) < dt.timedelta(4):
        print 'foo: ', sunday.month, sunday.day
        print "%s Sunday after Pentecost (Peter's Pence),%d/%d/%d,<a href=\'http://www.fisheaters.com/customstimeafterpentecost1.html\'>Time after Pentecost Overview</a> <a href=\'http://www.fisheaters.com/peterspence.html\'>(Peter's Pence)</a>" % (nth[i], sunday.month, sunday.day, sunday.year)
      elif sunday == dt.date(yr, 7, 22):
        print "%s Sunday after Pentecost (St. Mary Magdelen),%d/%d/%d,<a href=\'http://www.fisheaters.com/customstimeafterpentecost1.html\'>Time after Pentecost Overview</a> <a href=\'http://www.fisheaters.com/customstimeafterpentecost3x.html\'>(St. Mary Magdelen)</a>" % (nth[i], sunday.month, sunday.day, sunday.year)
      elif sunday == dt.date(yr, 7, 26):
        print "%s Sunday after Pentecost (St. Anne),%d/%d/%d,<a href=\'http://www.fisheaters.com/customstimeafterpentecost1.html\'>Time after Pentecost Overview</a> (St. Anne)" % (nth[i], sunday.month, sunday.day, sunday.year)
      elif sunday == dt.date(yr, 7, 29):
        print "%s Sunday after Pentecost (St. Martha),%d/%d/%d,<a href=\'http://www.fisheaters.com/customstimeafterpentecost1.html\'>Time after Pentecost Overview</a> <a href=\'http://www.fisheaters.com/customstimeafterpentecost5a.html\'>(St. Martha)</a>" % (nth[i], sunday.month, sunday.day, sunday.year)
      elif sunday == dt.date(yr, 8, 25):
        print "%s Sunday after Pentecost (King St. Louis IX),%d/%d/%d,<a href=\'http://www.fisheaters.com/customstimeafterpentecost1.html\'>Time after Pentecost Overview</a> <a href=\'http://www.fisheaters.com/customstimeafterpentecostsaintlouis.html\'>(King St. Louis IX)</a>" % (nth[i], sunday.month, sunday.day, sunday.year)
      elif sunday == dt.date(yr, 9, 19):
        print "%s Sunday after Pentecost (St. Januarius),%d/%d/%d,<a href=\'http://www.fisheaters.com/customstimeafterpentecost1.html\'>Time after Pentecost Overview</a> <a href=\'http://www.fisheaters.com/customstimeafterpentecost9.html\'>(St. Januarius)</a>" % (nth[i], sunday.month, sunday.day, sunday.year)
      elif sunday == dt.date(yr, 10, 4):
        print "%s Sunday after Pentecost (St. Francis),%d/%d/%d,<a href=\'http://www.fisheaters.com/customstimeafterpentecost1.html\'>Time after Pentecost Overview</a> <a href=\'http://www.fisheaters.com/feastofstfrancisofassisi.html\'>(St. Francis)</a>" % (nth[i], sunday.month, sunday.day, sunday.year)
      elif sunday == dt.date(yr, 10, 15):
        print "%s Sunday after Pentecost (St. Theresa),%d/%d/%d,<a href=\'http://www.fisheaters.com/customstimeafterpentecost1.html\'>Time after Pentecost Overview</a> (St. Francis)" % (nth[i], sunday.month, sunday.day, sunday.year)
      elif sunday == dt.date(yr, 10, 31):
        print "%s Sunday after Pentecost (Halloween),%d/%d/%d,<a href=\'http://www.fisheaters.com/customstimeafterpentecost1.html\'>Time after Pentecost Overview</a> <a href=\'http://www.fisheaters.com/customstimeafterpentecost12aa.html\'>(Halloween)</a>" % (nth[i], sunday.month, sunday.day, sunday.year)
      elif sunday == dt.date(yr, 11, 11):
        print "%s Sunday after Pentecost (Martinmas),%d/%d/%d,<a href=\'http://www.fisheaters.com/customstimeafterpentecost1.html\'>Time after Pentecost Overview</a> <a href=\'http://www.fisheaters.com/customstimeafterpentecost15.html\'>(Martinmas)</a>" % (nth[i], sunday.month, sunday.day, sunday.year)
      elif sunday == dt.date(yr, 11, 25):
        print "%s Sunday after Pentecost (St. Catherine),%d/%d/%d,<a href=\'http://www.fisheaters.com/customstimeafterpentecost1.html\'>Time after Pentecost Overview</a> <a href=\'http://www.fisheaters.com/customstimeafterpentecost14.html\'>(St.  Catherine)</a>" % (nth[i], sunday.month, sunday.day, sunday.year)
      else:
        print "%s Sunday after Pentecost,%d/%d/%d,<a href=\'http://www.fisheaters.com/customstimeafterepiphany1.html\'>Time after Pentecost Overview</a>" % (nth[i], sunday.month, sunday.day, sunday.year)
    i += 1
    sunday += dt.timedelta(7)

  # Other feasts throughout the year

  stbarbara = dt.date(yr-1, 12, 4)
  if stbarbara not in dates:
    dates.append(stbarbara)
    print "St. Barbara,%d/%d/%d,<a href=\'http://www.fisheaters.com/customsadvent2a.html\'>St. Barbara</a>" % (stbarbara.month, stbarbara.day, stbarbara.year)

  stnicholas = dt.date(yr-1, 12, 6)
  if stnicholas not in dates:
    dates.append(stnicholas)
    print "St. Nicholas,%d/%d/%d,<a href=\'http://www.fisheaters.com/customsadvent3.html\'>St. Nicholas</a>" % (stnicholas.month, stnicholas.day, stnicholas.year)

  guadalupe = dt.date(yr-1, 12, 12)
  if guadalupe not in dates:
    dates.append(guadalupe)
    print "Feast of Our Lady of Guadalupe,%d/%d/%d,<a href=\'http://www.fisheaters.com/customsadvent6.html\'>Feast of Our Lady of Guadalupe</a>" % (guadalupe.month, guadalupe.day, guadalupe.year)

  stlucy = dt.date(yr-1, 12, 13)
  if stlucy not in dates:
    dates.append(stlucy)
    print "St. Lucy,%d/%d/%d,<a href=\'http://www.fisheaters.com/customsadvent6a.html\'>St. Lucy</a>" % (stlucy.month, stlucy.day, stlucy.year)

  stanthonydesert = dt.date(yr, 1, 17)
  if stanthonydesert not in dates:
    dates.append(stanthonydesert)
    print "St. Anthony of the Desert,%d/%d/%d,St. Anthony of the Desert" % (stanthonydesert.month, stanthonydesert.day, stanthonydesert.year)

  stagnes = dt.date(yr, 1, 21)
  if stagnes not in dates:
    dates.append(stagnes)
    print "St. Agnes,%d/%d/%d,<a href=\'http://www.fisheaters.com/customstimeafterepiphany2.html\'>St. Agnes</a>" % (stagnes.month, stagnes.day, stagnes.year)

  stbrigid = dt.date(yr, 2, 1)
  if stbrigid not in dates:
    dates.append(stbrigid)
    print "St. Brigid,%d/%d/%d,<a href=\'http://www.fisheaters.com/customstimeafterepiphany2a.html\'>St. Brigid</a>" % (stbrigid.month, stbrigid.day, stbrigid.year)

  stblaise = dt.date(yr, 2, 3)
  if stblaise not in dates:
    dates.append(stblaise)
    print "St. Blaise,%d/%d/%d,<a href=\'http://www.fisheaters.com/customstimeafterepiphany4.html\'>St. Blaise</a>" % (stblaise.month, stblaise.day, stblaise.year)

  stvalentine = dt.date(yr, 2, 14)
  if stvalentine not in dates:
    dates.append(stvalentine)
    print "St. Valentine,%d/%d/%d,<a href=\'http://www.fisheaters.com/customstimeafterepiphany5.html\'>St. Valentine</a>" % (stvalentine.month, stvalentine.day, stvalentine.year)

  stpatrick = dt.date(yr, 3, 17)
  if stpatrick not in dates:
    dates.append(stpatrick)
    print "St. Patrick,%d/%d/%d,<a href=\'http://www.fisheaters.com/customslent4.html\'>St. Patrick</a>" % (stpatrick.month, stpatrick.day, stpatrick.year)

  walpurgisnacht = dt.date(yr, 4, 30)
  if walpurgisnacht not in dates:
    dates.append(walpurgisnacht)
    print "Walpurgisnacht,%d/%d/%d,<a href=\'http://www.fisheaters.com/walpurgisnacht.html\'>Walpurgisnacht</a>" % (walpurgisnacht.month, walpurgisnacht.day, walpurgisnacht.year)

  stanthony = dt.date(yr, 6, 13)
  if stanthony not in dates:
    dates.append(stanthony)
    print "St. Anthony of Padua,%d/%d/%d,<a href=\'http://www.fisheaters.com/customstimeafterpentecoststa.html\'>St.  Anthony of Padua</a>" % (stanthony.month, stanthony.day, stanthony.year)

  stmarymagdelen = dt.date(yr, 7, 22)
  if stmarymagdelen not in dates:
    dates.append(stmarymagdelen)
    print "St. Mary Magdelen,%d/%d/%d,<a href=\'http://www.fisheaters.com/customstimeafterpentecost3x.html\'>St. Mary Magdelen</a>" % (stmarymagdelen.month, stmarymagdelen.day, stmarymagdelen.year)

  stanne = dt.date(yr, 7, 26)
  if stanne not in dates:
    dates.append(stanne)
    print "St. Anne,%d/%d/%d,St. Anne" % (stanne.month, stanne.day, stanne.year)

  stmartha = dt.date(yr, 7, 29)
  if stmartha not in dates:
    dates.append(stmartha)
    print "St. Martha,%d/%d/%d,<a href=\'http://www.fisheaters.com/customstimeafterpentecost5a.html\'>St. Martha</a>" % (stmartha.month, stmartha.day, stmartha.year)

  stkinglouis = dt.date(yr, 8, 25)
  if stkinglouis not in dates:
    dates.append(stkinglouis)
    print "King St. Louis IX,%d/%d/%d,<a href=\'http://www.fisheaters.com/customstimeafterpentecostsaintlouis.html\'>King St. Louis IX</a>" % (stkinglouis.month, stkinglouis.day, stkinglouis.year)

  stjanuarius = dt.date(yr, 9, 19)
  if stjanuarius not in dates:
    dates.append(stjanuarius)
    print "St. Januarius,%d/%d/%d,<a href=\'http://www.fisheaters.com/customstimeafterpentecost9.html\'>St. Januarius</a>" % (stjanuarius.month, stjanuarius.day, stjanuarius.year)

  stfrancis = dt.date(yr, 10, 4)
  if stfrancis not in dates:
    dates.append(stfrancis)
    print "St. Francis,%d/%d/%d,<a href=\'http://www.fisheaters.com/feastofstfrancisofassisi.html\'>St. Francis</a>" % (stfrancis.month, stfrancis.day, stfrancis.year)

  sttheresa = dt.date(yr, 10, 15)
  if sttheresa not in dates:
    dates.append(sttheresa)
    print "St. Theresa,%d/%d/%d,St. Theresa" % (sttheresa.month, sttheresa.day, sttheresa.year)

  martinmas = dt.date(yr, 11, 11)
  if martinmas not in dates:
    dates.append(martinmas)
    print "Martinmas,%d/%d/%d,<a href=\'http://www.fisheaters.com/customstimeafterpentecost15.html\'>Martinmas</a>" % (martinmas.month, martinmas.day, martinmas.year)

  stcatherine = dt.date(yr, 11, 25)
  if stcatherine not in dates:
    dates.append(stcatherine)
    print "St. Catherine,%d/%d/%d,<a href=\'http://www.fisheaters.com/customstimeafterpentecost14.html\'>St. Catherine</a>" % (stcatherine.month, stcatherine.day, stcatherine.year)

  halloween = dt.date(yr, 10, 31)
  if halloween not in dates:
    dates.append(halloween)
    print "Halloween,%d/%d/%d,<a href=\'http://www.fisheaters.com/customstimeafterpentecost12aa.html\'>Halloween</a>" % (halloween.month, halloween.day, halloween.year)
