#include <stdio.h>
#include <arpa/inet.h>

//IPaddresss structure
struct in_addr{
    uint32_t s_addr; // address in network byte order
}

uint32_t htonl(uint32_t hostlong);
uint32_t htons(uint32_t hostshort);
return: value in network byte order

uint32_t ntohl(uint32_t netlong);
uint32_t ntohs(uint32_t netshort);
return: value in host byte order

int inet_pton(AF_INET, const char *src, void *dst);
    Returns: 1 if OK, 0 if src is invaild dotted decimal, -1 on error

const char *inet_ntop(AF_INET, const void *src, char *dstm, socklen_t size);
    Returns: pointer to a dotted string if OK, NULL on error



#include "csapp.h"

int main(int argc, char **argv) {
    struct in_addr inaddr;         // Address in network byte order
    uint16_t addr;                 // Adress in host byte order
    char buf[MAXBUF];              // Buffer for dotted-decimal string

    if (argc != 2){
        fprintf(stderr, "usage: %s <hex number>\n", argv[0]);
        exit(0);
    }
    sscanf(argv)
}

