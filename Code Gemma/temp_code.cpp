int isPrime(int n){
    for(int i=2;i*i<=n;i++){
        if(n%i==0)
            return false;
    }
    return true;
}

int FindPrimeNumber(int n){
    // start iterating from n
    for(int i=n;;i++){
        if(isPrime(i)){
            string s = to_string(i);
            string number = to_string(n);
            if(s.find(number)<s.size()){
                return i;
            }
        }
    }
}
main(){
    int n = 42;
    cout << FindPrimeNumber(n) << endl;
}
                                
                          