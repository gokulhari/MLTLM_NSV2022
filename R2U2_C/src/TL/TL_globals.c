/*=======================================================================================
** File Name:  TL_globals.c
**
** Title:  global variables for the TL engine
**
** $Author:    jschuman
** $Revision:  $
** $Date:      2016-6-16
**
**
** Purpose:
**	global variables for the TL engine
**
** Limitations, Assumptions, External Events, and Notes:
**	the global variables: instruction_mem and interval_mem
**	are located in auto-generated files TL_formula.c and TL_formula_int.c
**
**
** Modification History:
**   Date | Author | Description
**   ---------------------------
**
**=====================================================================================*/

#include "TL_observers.h"
#include "TL_queue_ft.h"
#include "TL_queue_pt.h"

timestamp_t t_now;

int r2u2_errno = 0;

atomics_vector_t atomics_vector;
atomics_vector_t atomics_vector_prev;

results_pt_t results_pt;
results_pt_t results_pt_prev;

results_rising_pt_t results_pt_rising;

box_queue_mem_pt_t pt_box_queue_mem;
box_queues_pt_t pt_box_queues;

sync_queues_ft_t ft_sync_queues;
SCQ_t SCQ;

instruction_mem_t instruction_mem_pt;
interval_mem_t interval_mem_pt;

/// \brief Stores decoded instructions from ftm.bin load a0 a1 timeaddr scratch
instruction_mem_t instruction_mem_ft;
/// \brief Stores decoded instructions from fti.bin, intervals - [1,2] in G[1,2]
/// etc.
interval_mem_t interval_mem_ft;
/// \brief stores decoded SCQ map stored in ftscq.bin
addr_SCQ_map_t addr_SCQ_map_ft;

#if R2U2_TL_Formula_Names
aux_str_map_t aux_str_map = {0};
aux_str_arena_t aux_str_arena = {0};
#endif

#if R2U2_TL_Contract_Status
aux_con_map_t aux_con_map = {0};
aux_con_arena_t aux_con_arena = {0};
aux_con_forms_t aux_con_forms = {0};
aux_con_max_t aux_con_max = 0;
#endif

#if R2U2_AT_Signal_Sets
aux_signal_set_map_t aux_signal_set_map = {0};
aux_signal_set_arena_t aux_signal_set_arena = {0};
#endif
