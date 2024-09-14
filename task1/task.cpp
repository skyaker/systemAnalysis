#include <iostream>
#include <fstream>
#include <sstream>
#include <vector>
#include <string>

std::string getValue(char* argv[]) {
  std::string filePath = argv[1];
  int rowNum = std::stoi(argv[2]);
  int colNum = std::stoi(argv[3]);

  std::ifstream csvFile(filePath);

  if (!csvFile.is_open()) {
    std::cout<<"File not found";
    return 0;
  }

  std::string lineElements;
  int currentLine = 0;

  while (std::getline(csvFile, lineElements)) {
    if (currentLine == rowNum) {
      std::stringstream lineString(lineElements);
      std::string currentElement;
      int currentCol = 0;

      while (std::getline(lineString, currentElement, ',')) {
        if (currentCol == colNum) {
          return currentElement;
        }
        currentCol++;
      }

      std::cout<<"Column is not found"<<std::endl;
    }
    currentLine++;
  }

  std::cout<<"Row is not found"<<std::endl;
}

int main(int argc, char* argv[]) {
  if (argc != 4) {
    std::cerr << "Usage: " << argv[0] << " <path_to_csv> <row> <column>" << std::endl;
    return 1;
  }

  std::cout<<"Answer: "<<getValue(argv);
}