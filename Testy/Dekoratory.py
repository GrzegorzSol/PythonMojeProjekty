
def dekor(funkcja):
  def wew():
    print("Dekorujemy funkcje")
    return funkcja()

  return wew

@dekor
def zwyklafunkcja():
  print("To jest zwykła funkcja")


zwyklafunkcja()
