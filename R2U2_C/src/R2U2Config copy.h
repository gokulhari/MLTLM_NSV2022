#ifndef R2U2_CONFIG_H
#define R2U2_CONFIG_H

/// \brief number of signals, related to L_SIG_ADDR
#define N_SIGS 256
/// \brief number atomics, related to L_ATOMIC_ADDR
#define N_ATOMICS 256
/// \brief number of instructions
#define N_INSTRUCTIONS 256
/// \brief number of at instructions
#define N_AT 256
/// \brief number of intervals
#define N_INTERVAL 128
/// \brief Length of opcode, codes for Until, Modered, Box (Global), Diamond,
/// And, Or, Implies (Future) etc.
#define L_OPC 5
/// Signal on two sides of opcode. Contains 2 bits for atomic, true or false, or
/// subformula, and 8 bits for the number following them, like a1 is 00- 0000001
#define L_OP 10
/// \brief This is a count on the interval of temporal operator. Suppose the say
/// the third until operator in the AST with CSE, then the 3 -1 = 2 will point
/// to the line in ts (fti.bin) for the line which contains the interval bounds.
#define L_INTVL 8
/// \brief Used only for temporal operators, stores the amount of scratch space
/// needed for temporal operators
#define L_SCRATCH 7
/// \brief Comparison, ==, >, >= etc, see atas.py.
#define L_COMP 3
/// \brief Length of filter, see list of filters in filters.py
#define L_FILTER 4
/// \brief max_const_width, ref in atas.py.
#define L_NUM 32
/// \brief The interval of temporal operators is denoted by two 16 bit numbers,
/// like in G[1,2], [1,2] is denoted by
/// 0000 0000 0000 0001 --- 0000 0000 0000 0010
/// and stored in fti.bin.
#define L_INTERVAL 32
/// \brief Max size of scq, the last line, last number in ftscq.bin.
#define L_SCQ_SIZE 2048
#define L_SCQ_ADDRESS 16
#define L_DOT_BUFFER 64
#define N_PT_QUEUES 128
#define TL_INF 1073676289
#define MAX_LINE 128
#define L_VARIABLE 8
#define N_FORMULAS 64
/// \brief max_at_width ref in atas.py
#define L_ATOMIC_ADDR 8
/// \brief sig_width, ref in atas.py
#define L_SIG_ADDR 8
/// \brief sum of L_OPC, L_OP, L_OP, L_INTVL, L_SCRATCH
#define L_INSTRUCTION 40
/// \brief Sum of L_ATOMIC_ADDR, L_FILTER, L_SIG_ADDR, L_COMP, L_NUM, N_NUM + 1
#define L_AT_INSTRUCTION 88
/// \brief sum of N_PT_QUEUES, L_DOT_BUFFER
#define N_DOT_BUFFERS_TOTAL 8192
/// \brief  the same as N_INSTRUCTIONS
#define N_SUBFORMULA_SNYC_QUEUES 256
#define N_AUX_STRINGS 256
#define L_AUX_STRINGS 4096
typedef double r2u2_input_data_t;
typedef unsigned int timestamp_t;
typedef char signal_names[N_SIGS * L_VARIABLE];
typedef char formula_names[N_FORMULAS * L_VARIABLE];

#endif