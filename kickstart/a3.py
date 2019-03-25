#include <iostream>
#include <vector>
using namespace std;
const int MOD=1000000007;
int powll(int base,int n){
    if (n==0) return 1;
    if (n==1) return base;
    long long tmp=powll(base,n/2);
    tmp=(tmp*tmp)%MOD;
    if (n%2==1) tmp=(tmp*base)%MOD;
    return int(tmp);
}
int geoSum(int base,int n){
    if (n==1) return base;
    long long tmp=geoSum(base,n/2);
    tmp=(tmp+tmp*powll(base,n/2))%MOD;
    if (n%2==1) tmp=(tmp+powll(base,n))%MOD;
    return int(tmp);
}

int main() {
    int no;
    cin>>no;
    for (int tt=1;tt<=no;tt++){
        long long n,k,x1,y1,c,d,e1,e2,f;
        cin>>n>>k;
        vector<long long> x(n),y(n);
        cin>>x[0]>>y[0]>>c>>d>>e1>>e2>>f;

        vector<long long> a(n);
        a[0]=(x[0]+y[0])%f;
        for (int i=1;i<n;i++) {
            x[i] = (c * x[i - 1] + d * y[i - 1] + e1) % f;
            y[i] = (d * x[i - 1] + c * y[i - 1] + e2) % f;
            a[i]=(x[i]+y[i])%f;
        }

        vector<long long> sum(n);
        sum[0]=geoSum(1,k);
        for (int i=1;i<n;i++) {
            sum[i]=(sum[i-1]+geoSum(i+1,k))%MOD;
        }

        long long ans=0;
        for (int i=0;i<n;i++){
            ans=(ans+(((n-i)*a[i])%MOD)*sum[i])%MOD;
        }

        cout<<"Case #"<<tt<<": "<<ans<<endl;
    }

    return 0;
}
