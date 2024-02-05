NX = 8
NZ = 7
SIM_TIME = 10 # 100
OUT_FREQ = 10
#DATA_SPEC = DATA_SPEC_ZEROS 
DATA_SPEC = DATA_SPEC_THERMAL

EXEC = serial.out
FILE=miniWeather_serial_test_solver.cpp

${EXEC}: ${FILE}
	# the tragedy of life is that we use mpic++ to compile a serial code
	mpic++ ${FILE} -D_NX=${NX} -D_NZ=${NZ} -D_SIM_TIME=${SIM_TIME} -D_OUT_FREQ=${OUT_FREQ} -D_DATA_SPEC=${DATA_SPEC} -o ${EXEC}

clean:
	/bin/rm serial.out

