#include <sys/ipc.h>
#include <sys/shm.h>
#include <unistd.h>
#include <stdlib.h>
#include <stdio.h>

int main(){
	int shm_id;
	size_t size=sizeof(double);
	int shmflg=IPC_CREAT | 0666;
	key_t key=12345;
	shm_id=shmget(key,size,shmflg);
	double *double_value;
	if(shm_id==-1){
		perror("ERROR: SHGET failed\n");
		exit(0);
	}
	
	double_value=shmat(shm_id,NULL,0);
	if(double_value==(double*)-1){
		perror("ERROR: SHAt failed\n");
		exit(0);
	}
	
	*double_value=34.5;
	while(*double_value==34.5){
		sleep(1);
	}
	if(shmdt(double_value)==-1){
		perror("ERROR: SHMDT failed\n");
		exit(0);
	}
	
	
	shmctl(shm_id,IPC_RMID,NULL);
	return 0;

}
