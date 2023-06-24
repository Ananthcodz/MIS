#include <stdio.h>
#include <conio.h>

int main(){
    int i , n, sum = 0, count = 0, y, quant, wt = 0, tat = 0, at[10],  bt[10], temp[10];
    float avg_wt, ang_tat;
    printf("The total number of processes: ");
    scanf("%d",&nop);
    y = nop;

    for(i = 0;i<nop;i++){
        printf("Enter the arrival time and busrt time of process %d",i+1);
        printf("Arrival time is: ");
        scanf("%d",&at[i]);
        printf("Busrt time is: ");
        scanf("%d",&bt[i]);
        temp[i] = bt[i];
    } 

    printf("Enter the time quantum for the processes: ");
    scanf("%d",&quant);

    printf("\n Process No \t\t Burst time \t\t TAT \t\t Waiting time");
    for (sum = 0,i=0;y!=0;){
        if(temp[i]<=quant && temp[i]>0){
            sum  = sum + temp[i];
            temp[i] = 0;
            count = 1;
        }

        else if (temp[i]>0){
            temp[i] = temp[i] - quant;
            sum = sum + quant;
        }

        if(temp[i]==0 && count == 1){
            y--;
            printf("\nProcess No[%d] \t\t %d \t\t\t\t %d \t\t\t %d",i+1,bt[i],sum - at[i],sum - at[i]-bt[i]);
            wt = wt+sum - at[i] - bt[i];
            tat = tat+sum - at[i];
            count = 0;
        }

        if(i == nop - 1){
            i = 0;
        }
        else if(at[i+1]<= sum){
            i++;
        }
        else{
            i = 0;
        }
    }

    avg_wt = wt*1.0/nop;
    avg_tat = tat* 1.0/nop;
    printf("\n Average waiting time: %f", avg_wt);
    printf("\n Average turn around time: %f",avg_tat);
    getch();
}