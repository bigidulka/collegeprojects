#include"Header.h"
int main()
{
	setlocale(0, "ru");
	string s; getline(cin, s);
	map<string, int> m;
	for (size_t i = 0; i < s.length(); i++) {
		int n{};
		for (size_t j = i; j < s.length(); j++) {
			if (s[j] != ' ') n++;
			else break;
		}
		string word{};
		for (size_t j = i; j < i + n; j++) {
			word += s[j];
		}
		i += word.length();
		m[word]++;
	}
	pair<string, int> maxValuePair;
	int maxValue = INT_MIN;
	for (auto& i : m)
		if (maxValue < i.second) {
			maxValue = i.second;
			maxValuePair = i;
		}
	cout << "Самое частое слово: " << maxValuePair.first << endl;
}