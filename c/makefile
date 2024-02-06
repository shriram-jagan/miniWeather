NX = 200
NZ = 100
SIM_TIME = 10
OUT_FREQ = 1
DATA_SPEC = DATA_SPEC_THERMAL

EXEC = serial.out
FILE = miniWeather_serial.cpp

${EXEC}: ${FILE}
	# the tragedy of life is that we use mpic++ to compile a serial code
	mpic++ ${FILE} -D_NX=${NX} -D_NZ=${NZ} -D_SIM_TIME=${SIM_TIME} -D_OUT_FREQ=${OUT_FREQ} -D_DATA_SPEC=${DATA_SPEC} -o ${EXEC}

clean:
	/bin/rm serial.out

