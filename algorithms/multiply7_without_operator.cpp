#include<iostream>

using namespace std;

int multiplynum(int n){
	// n*7 = n*(4+2+1) = n*4+n*2+n*1
	return (n<<2)+(n<<1)+(n<<0);

}

int main(){
	int num, final_ans;
	cout << "Enter a Number: "<<endl;
	cin >> num;
	final_ans = multiplynum(num);
	cout << final_ans << endl;
}
