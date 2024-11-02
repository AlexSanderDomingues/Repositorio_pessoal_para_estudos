#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main() {
    srand(time(NULL));
    int escolhamaquina, palpite, placarjog = 0, placarcom = 0, tentativas = 3;

    printf("------------------------------------\n");
    printf("Bem-vindo ao Jogo de Adivinhaçao!!\n");
    printf("------------------------------------\n");

    do {
        escolhamaquina = rand() % 10 + 1; // Gera número aleatório entre 1 e 10
        printf("\nPensando em um numero entre 1 e 10 ....\n");

        for (int i = 0; i < tentativas; i++) {
              escolhamaquina = rand() % 10 + 1;
            printf("Tentativa %d: Em que numero eu pensei? ", i + 1);
            scanf("%i", &palpite);

            if (escolhamaquina == palpite) {
                printf("Voce escolheu: %i\n Eu escolhi: %i\nVoce venceu!\n", palpite, escolhamaquina);
                placarjog++; // Incrementa placar do jogador
                break; // Sai do loop de tentativas se o jogador acertar
            } else {
                printf("Voce escolheu: %i\nEu escolhi: %i\n", palpite, escolhamaquina);
                if (i < tentativas - 1) {
                    printf("Tente novamente!\n"); // Mensagem se não for a última tentativa
                } else {
                    printf("Voce esgotou suas tentativas! Eu venci!\n");
                    placarcom++; // Incrementa placar da máquina se o jogador não acertar
                }
            }
        }

        printf("\nPlacar: %ix%i.\n", placarjog, placarcom);

    } while (placarcom < 3 && placarjog < 3); // Continua até que um dos placares atinja 3

    // Mensagem de vitória ou derrota após o loop
    if (placarjog == 3) {
        printf("Voce venceu o jogo!\n");
    } else {
        printf("Eu ganhei o jogo!\n");
    }

    return 0;
}
