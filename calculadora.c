
#include <stdio.h>

int main()
{
    int n1,n2,e,sm,sb,d,m;
    char r;
   do{
    printf("Bem-Vindo a Calculadora em C");//mensagem inicial
    printf("\nDigite seu Numero: ");//primeiro numero
    scanf("%i",&n1);//leitura
    printf("Digite outro Numero: ");//segundo numero
    scanf("%i",&n2);//leitura
    printf("Qual das seguintres operaçoes voce deseja fazer ?\n1)SOMA\n2)SUBTRAÇÃO\n3)DIVISÃO\n4)MULTIPLICAÇÃO\nDigite sua escolha: ");
    scanf("%i",&e);//leitura do sistema de escolhas implementado acima
    switch(e){//sistema de escolhas de operaçoes
        case 1:
        sm=n1+n2;
        printf("O resultado sera: %i",sm);
        break;
        case 2:
        sb=n1-n2 || n2-n1;
        printf("O resultado sera: %i",sb);
        break;
        case 3:
        if(n2!=0){
        d=n1/n2 || n2/n1;
        printf("O resultado sera: %i",d);
        break;
        }else{
            printf("Erro: Divisao por Zero\n");
            return 1;
        }
        
        
        case 4:
        m=n1*n2;
        printf("O resultado sera: %i",m);
        break;
    } 
     
     printf("\nDigite 0 para recomeçar ou qualquer tecla  para finalizar: ");//sistema de restart se digitar 0
    scanf(" %c",&r);
   }while(r=='0');
   printf("Volte sempre\n");
   
   
   
    return 0;
    
}
