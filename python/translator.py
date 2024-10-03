// Code in C++

string translate_to_alphabet() {
  string capital = ".....O";
  string decimal = "";
  string a = "O.....";
  string b = "O.O...";
  string c = "OO....";
string d = "";
string e = "";
string f = "";
string g = "";
string h = "";
string i = "";
string j = "";


}
string translate_to_braille(string s) {
  
}



int main (int argc, char* argv[]){
string s;
string tran[];

if (argv[2][0] == "." || argv[2][0] == "O") {
  istringstream iss{}
  tran = translate_to_alphabet();
} else {
  int i = 2;
  while (argv[i]) {
  
    ++i;
  }
  tran = translate_to_braille();
}

cout << tran;
}

// Code in python:

Braille = ['OO..','b','c','d','e','f','g','h','i','j',
			'k','l','m','n','o','p','q','r','s','t',
			'u','v','w','x','y','z', 
      'A','B','C','D','E','F','G','H','I','J',
      'K','L','M','N','O','P','Q','R','S','T',
      'U','V','W','X','Y','Z', 
      '0','1','2','3','4','5','6','7','8','9', 
      '.',',','?','!',':',';','-','/','<','>',
      '(',')',' ']

English = ['a','b','c','d','e','f','g','h','i','j',
			'k','l','m','n','o','p','q','r','s','t',
			'u','v','w','x','y','z', 
      'A','B','C','D','E','F','G','H','I','J',
      'K','L','M','N','O','P','Q','R','S','T',
      'U','V','W','X','Y','Z', 
      '0','1','2','3','4','5','6','7','8','9', 
      '.',',','?','!',':',';','-','/','<','>',
      '(',')',' ']
def translate_to_alphabet(BrailleText) :
	return ''.join([English[Braille.index(fi)] for ch in BrailleText for fi in braille if ch == fi])
def translate_to_alphabet(EnglishText) :
	return ''.join([Braille[English.index(fi)] for ch in EnglishText for fi in English if ch == fi])


