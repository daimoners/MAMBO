&DFT
  @IF ( ${BECKE_ACTIVE} == TRUE )
    @include becke_qs.inc
  @ENDIF
  @IF ( ${BECKE_ACTIVE} == FALSE )
    &QS
      METHOD GPW
      EPS_DEFAULT 1.0E-12
      MAP_CONSISTENT
      EXTRAPOLATION ASPC
      EXTRAPOLATION_ORDER 3
    &END QS
  @ENDIF
  BASIS_SET_FILE_NAME  BASIS_MOLOPT
  POTENTIAL_FILE_NAME  POTENTIAL
  @IF ( ${RESTART_WFN} == TRUE )
      WFN_RESTART_FILE_NAME ${WFN_FILE}
  @ENDIF
  LSD
  CHARGE ${CHARGE}
  !SURFACE_DIPOLE_CORRECTION
  !SURF_DIP_DIR Y
  &POISSON
       PERIODIC NONE
       PSOLVER WAVELET
  &END POISSON
  &MGRID
    CUTOFF 300
    NGRIDS 5
  &END MGRID
  &SCF
    @IF ( ${RESTART_WFN} == TRUE )
      SCF_GUESS RESTART
    @ENDIF
    @IF ( ${RESTART_WFN} == FALSE )
      SCF_GUESS ATOMIC
    @ENDIF
    EPS_SCF 1.0E-5
    CHOLESKY INVERSE_DBCSR
    MAX_SCF 100
    &OT ON
      ! DIIS convergence might not be constant with different mpiranks => use CG
      MINIMIZER CG
      PRECONDITIONER FULL_ALL
      ALGORITHM IRAC
    &END OT    
    &OUTER_SCF ON
        EPS_SCF 1.0E-5
        MAX_SCF 50
    &END
    &PRINT
      &RESTART
        FILENAME ./${PROJECT_NAME}
        BACKUP_COPIES 0
        COMMON_ITERATION_LEVELS 1
        &EACH 
          JUST_ENERGY ${WRITE_WFN}
          QS_SCF 0
        &END EACH
      &END RESTART
      &RESTART_HISTORY OFF
      &END RESTART_HISTORY
    &END PRINT
  &END SCF
  &XC
    &XC_FUNCTIONAL PBE
    &END XC_FUNCTIONAL
    &XC_GRID
      XC_DERIV SPLINE2
      XC_SMOOTH_RHO NONE
    &END XC_GRID
  &END XC
  &PRINT
    &MULLIKEN OFF
    &END MULLIKEN
    &HIRSHFELD ON
    &END HIRSHFELD 
    @IF ( ${WRITE_CUBE} == TRUE )
      &E_DENSITY_CUBE ON
         STRIDE 2 2 2 
      &END E_DENSITY_CUBE 
    @ENDIF
  &END PRINT
&END DFT 
&PRINT
  &FORCES ON
  &END
&END