#include<iostream>
#include<queue>
#include <cstring>
#define inf 0x3f3f3f3f
#define N 100005
#define rep(i,x,y) for (register int i=x;i<=y;++i) 
using namespace std; 

int n,k,lis,ans,pre[N],suf[N],a[N],t,T; 

priority_queue<pair< int ,int >,vector< pair < int ,int > >,greater<pair< int ,int > > > q; 
int main(){ 
	scanf("%d",&T); 
	while(T--){
		scanf("%d%d",&n,&k); 	
		ans=0; lis=0;
		memset(pre,0,sizeof(pre)); 
		memset(suf,0,sizeof(suf));
		while (q.size()) q.pop(); 
		rep(i,1,n) {
			scanf("%d",&t); a[i]=t-lis; lis=t; 
			pre[i]=i-1,suf[i]=i+1;  
		}
		pre[2]=suf[n]=0; 
		for(register int i=2;i<=n;++i) q.push(make_pair(a[i],i)); 
		for(register int i=1;i<=k;++i) {
			while (q.top().first!=a[q.top().second]) q.pop(); 
			pair< int ,int > e=q.top(); q.pop(); ans+=e.first; 
			int l=pre[e.second],r=suf[e.second]; 
			a[e.second]=(l&&r)?min(a[l]+a[r]-a[e.second],inf):inf; a[l]=a[r]=inf; 
			suf[pre[e.second]=pre[l]]=e.second,pre[suf[e.second]=suf[r]]=e.second;
			q.push(make_pair(a[e.second],e.second)); 
		}
		printf("%d\n",ans); 
		
	}
}