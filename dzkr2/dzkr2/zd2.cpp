//#include"header.h"
//int main()
//{
//	setlocale(0, "ru");
//	string s; getline(cin, s);
//	map<string, int> m;
//	for (size_t i = 0; i < s.length(); i++) {
//		int n{};
//		for (size_t j = i; j < s.length(); j++) {
//			if (s[j] != ' ') n++;
//			else break;
//		}
//		string word = s.substr(i, n);
//		i += word.length();
//		m[word]++;
//	}
//	pair<string, int> maxvaluepair;
//	int maxvalue = INT_MIN;
//	for (auto& i : m)
//		if (maxvalue < i.second) {
//			maxvalue = i.second;
//			maxvaluepair = i;
//		}
//	cout << "самое частое слово: " << maxvaluepair.first << endl;
//}