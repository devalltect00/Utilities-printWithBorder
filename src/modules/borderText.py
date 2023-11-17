import math

class borderText:
  def  __init__(self, innerText, defaultCharacterLengthHorizontally=None):
    self.innerText = innerText
    if defaultCharacterLengthHorizontally:
      self.lengthCharacterHorizontally = defaultCharacterLengthHorizontally
    else:
      self.setAppropriateCharacterLengthHorizontally()
  
  def setAppropriateCharacterLengthHorizontally(self):
    maxLength = max([len(text) for text in self.innerText])
    self.lengthCharacterHorizontally = maxLength + 4

  def draw(self):
    self.outputText = ""
    innerTextLength = len(self.innerText)
    for i in range(-1, innerTextLength+1):
      self.outputText += "\n"
      lengthCharacterHorizontally = self.lengthCharacterHorizontally-2
      borderTop = f"+{'='*(lengthCharacterHorizontally)}+"
      blankSpace = f"|{' '*(lengthCharacterHorizontally)}|"
      if i == -1:
        self.outputText += borderTop + "\n"
        self.outputText += blankSpace
      elif i == innerTextLength:
        self.outputText += blankSpace + "\n"
        self.outputText += borderTop
      else:
        iText = self.innerText[i]
        startNumberOfSpace, finalNumberOfSpace = self.determineNumberOfSpace(availableSpaceColumn = lengthCharacterHorizontally, textLength = len(iText))
        self.outputText += f"|{' '*startNumberOfSpace}{iText}{' '*finalNumberOfSpace}|"
    
    self.outputText += "\n\n"
    print(self.outputText)

  def saveText(self, output_file_path):
    with open(output_file_path, 'w') as outputFile:
        outputFile.write(self.outputText)

  @staticmethod
  def determineNumberOfSpace(availableSpaceColumn, textLength):
    startNumberOfSpace = (availableSpaceColumn - textLength)//2
    finalNumberOfSpace = math.ceil((availableSpaceColumn - textLength)/2)
    return (startNumberOfSpace, finalNumberOfSpace)

if __name__ == '__main__':
  # Example List
  '''
  [
        f"TOTAL TABLE: ",
        f"NUMBER OF COLUMN: ",
        f"NUMBER OF ROW: "
      ]
  '''

  listText = [
        f"TOTAL TABLE: ",
        f"NUMBER OF COLUMN: ",
        f"NUMBER OF ROW: "
      ]

  ptf = borderText(listText)
  ptf.draw()


