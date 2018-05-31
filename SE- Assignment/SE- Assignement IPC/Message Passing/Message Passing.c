#include <sys/ipc.h>
#include <sys/shm.h>
#include <unistd.h>
#include <stdlib.h>
#include <stdio.h>


#define READ 0
#define WRITE 1

int main(){
	int fd[2];
	pid_t pid;
	
	pipe(fd);
	pid=fork();
	
	
	int read_value;
	if(pid==0){
		//child Process
		close(fd[WRITE]);
		read(fd[READ],&read_value,sizeof(int));
		printf("The read value is %d\n",read_value);
	}else{
		//Parent Process
		int int_value=32;
		close(fd[READ]);
		write(fd[WRITE],&int_value,sizeof(int));

	
	}



	return 0;
}
