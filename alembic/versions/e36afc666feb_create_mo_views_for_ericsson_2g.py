"""Create MO views for Ericsson 2G

Revision ID: e36afc666feb
Revises: cb540db6ffbf
Create Date: 2018-05-15 05:37:36.889000

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e36afc666feb'
down_revision = 'cb540db6ffbf'
branch_labels = None
depends_on = None



class ReplaceableObject(object):
    def __init__(self, name, sqltext):
        self.name = name
        self.sqltext = sqltext


bsc = ReplaceableObject(
    'ericsson_cm_2g."BSC"',
    """

    SELECT 
        "FileName",
        "capabilities",
        "varDateTime",
        "subnetwork",
        "domain",
        "set",
        "AFRVAMOS",
        "AHRVAMOS",
        "AWBVAMOS",
        "ALPHA",
        "AMRCSFR3MODE",
        "AMRCSFR3THR",
        "AMRCSFR3HYST",
        "AMRCSHR3ICM",
        "AMRCSHR4ICM",
        "AMRCSFR3ICM",
        "AMRCSFR4ICM",
        "AMRCSFR4MODE",
        "AMRCSFR4THR",
        "AMRCSFR4HYST",
        "AMRCSHR3MODE",
        "AMRCSHR3THR",
        "AMRCSHR3HYST",
        "AMRCSHR4MODE",
        "AMRCSHR4THR",
        "AMRCSHR4HYST",
        "AMRFRSUPPORT",
        "AMRHRSUPPORT",
        "AMRSPEECHVERUSE",
        "AQMSUPPORT",
        "AQMMINBUFF",
        "AQMRTTCONST",
        "AQMMAXIPSIZE",
        "AQMMINIPSIZE",
        "REEST",
        "REPFACCH",
        "AMRCSWB1ICM",
        "AMRCSWB1HYST",
        "AMRCSWB1THR",
        "AMRWBDHA",
        "AMRWBSUPPORT",
        "AMRWBFB",
        "AMRWBSPVERUSE",
        "AMRWBPRIO",
        "AMRWBDYMAPRIO",
        "AFLP_TIME",
        "EITADMCTRL",
        "EITGMAXUSEUL",
        "EITEMAXUSEUL",
        "EITGMAXUSEDL",
        "EITEMAXUSEDL",
        "EITQOSPRIO",
        "BCCHNORMAL",
        "BSC_NAME",
        "BSCAFLP",
        "BSCAIRCT",
        "BSCFSOFFSETLSW",
        "BSCFSOFFSETMSW",
        "BSCMC",
        "BSSRELEASE",
        "CAP",
        "CHCODING",
        "CNID",
        "COEXUMTS",
        "COEXUMTSLSH",
        "COEXUMTSTINT",
        "CONFMODE",
        "GPRSEDAACT",
        "GPRSNWMODE",
        "DCA_STATE",
        "DISPP",
        "DN",
        "DLDELAY",
        "DTCBSC",
        "DTXFUL",
        "REGINTDL",
        "REGINTUL",
        "SSLENDL",
        "SSLENUL",
        "QLENDL",
        "QLENUL",
        "EFRVAMOS",
        "EMRSTATE",
        "EBANDINCLUDED",
        "EITHIGHCS",
        "EITSCHEDFREQH",
        "EITSCHEDFREQL",
        "ESDELAY",
        "FRVAMOS",
        "FBCHALLOC",
        "FASTRET3GNC2",
        "ONDEMANDGPHDEV",
        "GSM1800_ASSOC",
        "GSM1800_EVALTYPE",
        "GSM1800_IBHOASS",
        "GSM1800_IBHOSICH",
        "GSM1800_IHOSICH",
        "GSM1800_NHO",
        "GSM1800_TAAVELEN",
        "GSM1800_TALLOC",
        "GSM1800_THO",
        "GSM1800_TINIT",
        "GSM1800_TURGEN",
        "EGPRSIRUL",
        "EMERGPRL",
        "ENHAMRSIGN",
        "EXTCELLNO",
        "EXTHANDOVERNO",
        "GPRS5TSDLACT",
        "GPRSAVAINT",
        "GPRSNEUTRALACT",
        "GSM900_ASSOC",
        "GSM900_EVALTYPE",
        "GSM900_IBHOASS",
        "GSM900_IBHOSICH",
        "GSM900_IHOSICH",
        "GSM900_NHO",
        "GSM900_TAAVELEN",
        "GSM900_TALLOC",
        "GSM900_THO",
        "GSM900_TINIT",
        "GSM900_TURGEN",
        "GSM800_ASSOC",
        "GSM800_EVALTYPE",
        "GSM800_IBHOASS",
        "GSM800_IBHOSICH",
        "GSM800_IHOSICH",
        "GSM800_NHO",
        "GSM800_TAAVELEN",
        "GSM800_TALLOC",
        "GSM800_THO",
        "GSM800_TINIT",
        "GSM800_TURGEN",
        "G_SYS_TYPE",
        "HALFRATESUPP",
        "HCSCHAVAILTIMER",
        "HCSBAND1",
        "HCSBAND2",
        "HCSBAND3",
        "HCSBAND4",
        "HCSBAND5",
        "HCSBAND6",
        "HCSBAND7",
        "HCSBAND8",
        "HCSBANDHYST",
        "HCSBANDTHR1",
        "HCSBANDTHR2",
        "HCSBANDTHR3",
        "HCSBANDTHR4",
        "HCSBANDTHR5",
        "HCSBANDTHR6",
        "HCSBANDTHR7",
        "HCSBANDTHR8",
        "HCSTRAFDISSTATE",
        "HIGHFERULAWB",
        "HIGHFERDLAWB",
        "HOREQLACCI",
        "HRVAMOS",
        "HOMTD",
        "MAXTGCL",
        "MCIMALG",
        "INTCELLNO",
        "INTHANDOVERNO",
        "LOADOPT",
        "LOASNO",
        "LOPTETHR",
        "LOPTGTHR",
        "LQCACT",
        "LQCHIGHMCS",
        "LQCMODEUL",
        "LQCMODEDL",
        "LQCDEFAULTMCSDL",
        "LQCDEFAULTMCSUL",
        "LQCDEFMCSDLE2A",
        "LQCDEFMCSULE2A",
        "LQCHIGHMCSDLE2A",
        "LQCHIGHMCSULE2A",
        "LQCUNACK",
        "LS_STATUS",
        "MAXCELLSINLAYER",
        "MAXCHDATARATE",
        "MAXDBDEVINLAYER",
        "MAXNOCHGRP",
        "MAXNOSDCCHTRX",
        "MAXPWRUTDOA",
        "MCPABCCHOFF",
        "MBCRAC",
        "MNCDIGITHAND",
        "MODE",
        "MODHOTOHCS",
        "MSC_NAME",
        "MSCPOOL_ID",
        "MSEITRESPTIME",
        "MSQHOPRIO",
        "MSQUEUING",
        "NACCACT",
        "NOTIFP",
        "OF_ABISOPT",
        "OF_ADAPTCONF",
        "OF_ADMCTRL",
        "OF_REDPACLAT",
        "OF_RLINKTIMERAMR",
        "OF_AUTOFLP",
        "OF_AUTOIRCT",
        "OF_RPWRHO",
        "OF_AMR",
        "OF_AMRHR",
        "OF_AMRPWRCTRL",
        "OF_AMRWB",
        "OF_AMRWBMAXTRAFFIC",
        "OF_ATHAABIS",
        "OF_AUTOHFSEXPAND",
        "OF_TIGHTBCCHREUSE",
        "OF_BCCHPS",
        "OF_BTSPS",
        "OF_BTSPWRCTRL",
        "OF_COMBCRESUMTS",
        "OF_COMBINEDCELL",
        "OF_CAPCNTRLVAMOS",
        "OF_CRESLTE",
        "OF_DAMRREDUCE",
        "OF_DTM",
        "OF_DTMMSCLASS11",
        "OF_DYMA",
        "OF_DYNHRALLOC",
        "OF_DYNHRALLOCWB",
        "OF_DYNOLULSC",
        "OF_EFTA",
        "OF_EGPRS2ABPCLIMIT",
        "OF_EGPRSBPCLIMIT",
        "OF_EPOG",
        "OF_ENHAMRCOV",
        "OF_EXTNUMCELL",
        "OF_FEATSYNCHRNW",
        "OF_FF_CHAVSUALENH",
        "OF_FLEXABIS",
        "OF_FASTRETURN3G",
        "OF_G1GSMBAND",
        "OF_GPRS",
        "OF_GPRS5TSDL",
        "OF_GPRSAQM",
        "OF_ENHOSUCCRATE",
        "OF_GPRSNEUTRAL",
        "OF_GPRSCS3CS4",
        "OF_GPRSEDA",
        "OF_GPRSEIT",
        "OF_GPRSLOADOPT",
        "OF_GPRSPULS",
        "OF_GPRSQOS",
        "OF_HCS",
        "OF_HCSBAND",
        "OF_HDRATE",
        "OF_HPBOOST",
        "OF_HRC",
        "OF_HSCSD",
        "OF_IM3G",
        "OF_INCRSDCCHCAP",
        "OF_ISHOLSH",
        "OF_IURG",
        "OF_MAIOMANAGEMENT",
        "OF_MAXNUMCELLS",
        "OF_MCPAPS",
        "OF_MIP",
        "OF_MIPROUTE",
        "OF_MIXEDMODERADIO",
        "OF_MSPWRCTRL",
        "OF_MULTIBANDCELL",
        "OF_NACC",
        "OF_PMSQ",
        "OF_PFASTMSREG",
        "OF_PKTCELLPLAN",
        "OF_VGCSPMR",
        "OF_PREEMPTION",
        "OF_RANDOMFILL",
        "OF_QOSSTREAM",
        "OF_SBHO",
        "OF_SEMIPDCH",
        "OF_SPIDPRIO",
        "OF_SUPCOEXUMTS",
        "OF_SUPIRC",
        "OF_SQPRIO",
        "OF_SQSSUPPORT",
        "OF_TCHOPT",
        "OF_TFO",
        "OF_EGPRSIRU",
        "OF_XRANGEC",
        "OF_XRANGESC",
        "OF_EMRSUPPORT",
        "OF_VGCSDYNAMIC",
        "OF_VGCSENCR",
        "OF_VGCSTALKID",
        "OF_NC2PROFILE1",
        "OF_NC2PROFILE2",
        "OF_NC2PROFILE3",
        "OF_NC2PROFILE4",
        "OF_NC2PROFILE5",
        "OF_NC2PROFILE6",
        "OF_NC2PROFILE7",
        "OF_NC2PROFILE8",
        "OF_NC2PROFILE9",
        "OF_NC2PROFILE10",
        "OF_NC2PROFILE255",
        "OF_MCNSUPPORT",
        "OF_UTDOA",
        "OF_VAMOSADVANCED",
        "OF_VAMOSMAXTRAFFIC",
        "OF_FF_USERDATA",
        "OP_MODE",
        "OF_FF_TDSCDMA",
        "OF_FF_CRESTDSCDMA",
        "OF_WCDMAQUEUE",
        "PART",
        "PAGPRIO",
        "PCUQOS",
        "PILTIMERFLEX",
        "PILTIMER",
        "NSEIRELATION",
        "PMRSUPP",
        "PSCELLPLAN",
        "GSM1900_ASSOC",
        "GSM1900_EVALTYPE",
        "GSM1900_IBHOASS",
        "GSM1900_IBHOSICH",
        "GSM1900_IHOSICH",
        "GSM1900_NHO",
        "GSM1900_TAAVELEN",
        "GSM1900_TALLOC",
        "GSM1900_THO",
        "GSM1900_TINIT",
        "GSM1900_TURGEN",
        "PCUEIT",
        "RAND",
        "SACCHDLTHR",
        "RNC",
        "SP",
        "SACCHULTHR",
        "SBHOACTIVE",
        "SPEECHVERUSED",
        "SS_SDCCH_STATE",
        "SS_SDCCHACL",
        "SS_SDCCHPL",
        "SS_TCH_STATE",
        "SS_TCHACL",
        "SS_TCHPL",
        "SMPC",
        "TCHOPTIMIZATION",
        "TBFMODEACT",
        "HSCSDUPGTIMER",
        "PHHSCSD",
        "PHSTATE",
        "BADQDL",
        "BADQUL",
        "LOWSSDL",
        "LOWSSUL",
        "FASTASSIGN",
        "MAXLOAD",
        "TIMER3105",
        "NOOFPHYSINFOMSG",
        "CLMRKMSG",
        "CLSTIMEINTERVAL",
        "TRACEMSGTYPE",
        "SPEQINDCOLLECT",
        "SPIDTABLE",
        "TABLEID",
        "TSTATE",
        "SPID_ACTION",
        "GPRIO",
        "TALKID",
        "TFOPRIO",
        "TEITPENDING",
        "TFILIMIT",
        "TBFDLLIMIT",
        "TBFULLIMIT",
        "TIMERT3TRC",
        "TRXOFFDELAY",
        "TRXOFFTARGET",
        "TRXONTARGET",
        "PULSCHEDINT",
        "QASSTIME",
        "QOSMAPPING",
        "QOSSTREAMPRIO",
        "QOSCONVPRIO",
        "QOSTHP1",
        "QOSTHP2",
        "THPMBRFACTOR",
        "RNDFILL",
        "TRC",
        "ULDELAY",
        "USFLIMIT",
        "UTRANEXTCELLNO",
        "UTRANNRELNO",
        "UPDWNRATIO",
        "TSTREAMSTART",
        "TSTREAMPENDING",
        "UTDOAMRMODE",
        "VAMOSBSCSTATE",
        "VAMOSMAXTRAFFIC_CLAL",
        "VAMOSMAXTRAFFIC_CLTHR",
        "CAPACITYLOCKS",
        "VERSION",
        "VGENCR",
        "VGPRECEDE",
        "VGPRIO",
        "OF_INTERBSCNACC",
        "OF_REDLAT",
        "OF_FF_MIXHOP",
        "OF_DCDL",
        "OF_IMSIHO",
        "BSCIMSIHO",
        "IMSIPATA",
        "IMSIPATB",
        "IMSIPATC",
        "IMSIPATD",
        "NCCPERMA",
        "NCCPERMB",
        "NCCPERMC",
        "NCCPERMD",
        "OF_CAPCNTRLSCC",
        "OF_EFR",
        "OF_EMERGENCYMODE",
        "AMRFRMAXTRAFFIC",
        "AMRHRMAXTRAFFIC",
        "EFRMAXTRAFFIC",
        "HRMAXTRAFFIC",
        "AMRFRMAXTRAFFIC_CLAL",
        "AMRFRMAXTRAFFIC_CLTHR",
        "AMRHRMAXTRAFFIC_CLAL",
        "AMRHRMAXTRAFFIC_CLTHR",
        "AMRWBMAXTRAFFIC_CLAL",
        "AMRWBMAXTRAFFIC_CLTHR",
        "HRMAXTRAFFIC_CLAL",
        "HRMAXTRAFFIC_CLTHR",
        "EFRMAXTRAFFIC_CLAL",
        "EFRMAXTRAFFIC_CLTHR",
        "OF_MULTICCCH",
        "PAGBUNDLE",
        "OF_SMSCBADVANCED",
        "SMSCBS",
        "OF_PSDLPC",
        "OF_FASTRETURNLTE",
        "OF_LTEGSMNACC",
        "LTEGSMNACCSTATUS",
        "OF_BTSSOFTSYNC",
        "OF_EPU",
        "OF_APSULPC"
    FROM
    ericsson_cnaiv2."bsc"

    """
)

channel_group = ReplaceableObject(
    'ericsson_cm_2g."CHANNEL_GROUP"',
    """

    SELECT 
        "FileName",
        "capabilities",
        "varDateTime",
        "subnetwork",
        "domain",
        "set",
        "USERDATA",
        "BAND",
        "BCCD",
        "CBCH",
        "CELL_NAME",
        "CHGR_NAME",
        "BSC_NAME",
        "DCHNO",
        "EACPREF",
        "EXCHGR",
        "HOP",
        "HSN",
        "MAIO",
        "NUMREQBPC",
        "NUMREQE2ABPC",
        "NUMREQEGPRSBPC",
        "NUMREQCS3CS4BPC",
        "ODPDCHLIMIT",
        "SAS",
        "SDCCH",
        "SCTYPE",
        "STATE",
        "TG_NAME",
        "TN",
        "TN7BCCH",
        "TSC",
        "HOPTYPE",
        "ETCHTN",
        "CCCH",
        "TNBCCH",
        "BSPWRT"
    FROM
    ericsson_cnaiv2."channel_group"

    """
)

external_cell = ReplaceableObject(
    'ericsson_cm_2g."EXTERNAL_CELL"',
    """

    SELECT 
        "FileName",
        "capabilities",
        "varDateTime",
        "subnetwork",
        "domain",
        "set",
        "USERDATA",
        "AW",
        "BCC",
        "BCCHNO",
        "BSC_NAME",
        "BSPWR",
        "BSRXMIN",
        "BSRXSUFF",
        "BSTXPWR",
        "CELL_NAME",
        "CI",
        "C_SYS_TYPE",
        "DFI",
        "FASTMSREG",
        "EXTPEN",
        "LAC",
        "LAYER",
        "LAYERHYST",
        "LAYERTHR",
        "MCC",
        "MISSNM",
        "MNC",
        "MSRXMIN",
        "MSRXSUFF",
        "MSTXPWR",
        "NCC",
        "PHCSTHR",
        "PLAYER",
        "PSSTEMP",
        "PTIMTEMP",
        "RAC",
        "RIMNACC",
        "SCHO"
    FROM
    ericsson_cnaiv2."external_cell"

    """
)

inner_cell = ReplaceableObject(
    'ericsson_cm_2g."INNER_CELL"',
    """

    SELECT 
        "FileName",
        "capabilities",
        "varDateTime",
        "subnetwork",
        "domain",
        "set",
        "USERDATA",
        "CELL_NAME",
        "BSC_NAME",
        "CI",
        "CO",
        "EA",
        "EC",
        "LAC",
        "LOCNO",
        "MCC",
        "MNC",
        "MSC_NAME",
        "NCS",
        "RME",
        "RO"
    FROM
    ericsson_cnaiv2."inner_cell"

    """
)

internal_cell = ReplaceableObject(
    'ericsson_cm_2g."INTERNAL_CELL"',
    """

    SELECT 
        "FileName",
        "capabilities",
        "varDateTime",
        "subnetwork",
        "domain",
        "set",
        "USERDATA",
        "ACC",
        "ACCMIN",
        "ACSTATE",
        "ACTIVE",
        "AFLP",
        "AIRCT",
        "AGBLK",
        "ALLOCPREF",
        "AMRPCSTATE",
        "ANTENNA_GAIN",
        "ANTENNA_TILT",
        "ANTENNA_TYPE",
        "AQPSKONBCCH",
        "ASSV",
        "ATHABISPR",
        "ATT",
        "AW",
        "BCC",
        "BCCHDTCB",
        "BCCHDTCBHYST",
        "BCCHLOSS",
        "BCCHLOSSHYST",
        "BCCHNO",
        "BCCHREUSE",
        "BCCHTYPE",
        "BPDCHBR",
        "BSC_NAME",
        "BSPWR",
        "BSPWRB",
        "BSPWRMIN",
        "BSPWRT",
        "BPCDEL",
        "BSRPWRHO",
        "BSRPWROFFSET",
        "BSRXMIN",
        "BSRXSUFF",
        "BTSPSHYST",
        "BTSPS",
        "BSTXPWR",
        "CB",
        "CBCHD",
        "CBQ",
        "CCHPWR",
        "CELL_DIR",
        "CELL_NAME",
        "CELL_STATE",
        "CELL_TYPE",
        "CELLQ",
        "CHAP",
        "CHCSDL",
        "CHMAX",
        "CI",
        "CLSACC",
        "CLSLEVEL",
        "CLSRAMP",
        "CLS_STATUS",
        "CLTHV",
        "CODECREST",
        "CMDR",
        "CP_BCC_TSC",
        "CRH",
        "CRO",
        "CSPSALLOC",
        "CSPSPRIO",
        "C_SYS_TYPE",
        "DAMRCRABISPR",
        "DHA",
        "DHASS",
        "DHASSTHRASS",
        "DHASSTHRHO",
        "DHPR",
        "DISPLAY_TAG",
        "DTHAMR",
        "DTHNAMR",
        "DMPR",
        "DMQB",
        "DMQBAMR",
        "DMQBNAMR",
        "DMQG",
        "DMQGAMR",
        "DMQGNAMR",
        "DMSUPP",
        "DMTFAMR",
        "DMTFNAMR",
        "DMTHAMR",
        "DMTHNAMR",
        "DTMSTATE",
        "DTXD",
        "DTXU",
        "DYNBTSPWR_STATE",
        "DYNMSPWR_STATE",
        "DYNVGCH",
        "EFTASTATE",
        "E2AFACTOR",
        "E2APDCHBR",
        "E2ALQC",
        "E2AINITMCS",
        "ECSC",
        "EFACTOR",
        "EINITMCS",
        "EITEXCLUDED",
        "ENV_CHAR",
        "EPDCHBR",
        "FASTMSREG",
        "FASTRET3G",
        "FBOFFS",
        "FBVGCHALLOC",
        "FDDMRR",
        "FDDQMIN",
        "FDDQOFF",
        "FDDQMINOFF",
        "FDDRSCPMIN",
        "FDDREPTHR2",
        "FLEXHIGHGPRS",
        "FERLEN",
        "FNOFFSET",
        "FPDCH",
        "FULLAQPSK",
        "GAMMA",
        "GPDCHBR",
        "GPRSPRIO",
        "GPRSSUP",
        "HCSIN",
        "HCSOUT",
        "HEIGHT",
        "HOCLSACC",
        "HPBSTATE",
        "HYSTSEP",
        "IAN",
        "ICMSTATE",
        "IDLE",
        "IHO",
        "INTAVE",
        "IRC",
        "ISHOLEV",
        "LA",
        "LAC",
        "LATITUDE",
        "LAYER",
        "LAYERHYST",
        "LAYERTHR",
        "LCOMPDL",
        "LCOMPUL",
        "LIMIT1",
        "LIMIT2",
        "LIMIT3",
        "LIMIT4",
        "LONGITUDE",
        "MAXIHO",
        "MAXISHO",
        "MAXLAPDM",
        "MAXRET",
        "MAXSBLK",
        "MAXSMSG",
        "MAXTA",
        "MAX_ALTITUDE",
        "MAX_CELL_RADIUS",
        "MBCR",
        "MC",
        "MCC",
        "MFRMS",
        "MIN_ALTITUDE",
        "MINREQTCH",
        "MCPAPS",
        "MCPAPSHYST",
        "MISSNM",
        "MNC",
        "MSRPWRHO",
        "MSRPWROFFSET",
        "MSRXMIN",
        "MSRXSUFF",
        "MSTXPWR",
        "NCC",
        "NCCPERM",
        "NCSTAT",
        "NCRPT",
        "NCPROF",
        "NECI",
        "NUMTS",
        "NUMEGPRSTS",
        "OPTMSCLASS",
        "OWNBCCHINACT",
        "OWNBCCHINIDLE",
        "PHCSTHR",
        "PLAYER",
        "PLMNNAME",
        "PRACHBLK",
        "PRIMPLIM",
        "PSKONBCCH",
        "PSSBQ",
        "PSSHF",
        "PSSTA",
        "PSSTEMP",
        "PT",
        "PTIMBQ",
        "PTIMHF",
        "PTIMTA",
        "PTIMTEMP",
        "QBAHRV",
        "QBAWBV",
        "QBNAV",
        "QDESDLOV",
        "QDESULOV",
        "QBAFRV",
        "QCOMPDL",
        "QCOMPUL",
        "QDESDL",
        "QDESDLAFR",
        "QDESDLAHR",
        "QDESDLAWB",
        "QDESUL",
        "QDESULAFR",
        "QDESULAHR",
        "QDESULAWB",
        "QEVALSD",
        "QEVALSI",
        "QLENGTH",
        "QLENSD",
        "QLENSI",
        "QLIMDL",
        "QLIMDLAFR",
        "QLIMDLAWB",
        "QLIMUL",
        "QLIMULAFR",
        "QLIMULAWB",
        "QOFFSETDL",
        "QOFFSETDLAFR",
        "QOFFSETDLAWB",
        "QOFFSETUL",
        "QOFFSETULAFR",
        "QOFFSETULAWB",
        "QSC",
        "QSCI",
        "QSI",
        "RTTI",
        "REPPERNCH",
        "RESLIMIT",
        "RHYST",
        "RLINKT",
        "RLINKTAFR",
        "RLINKTAHR",
        "RLINKTAWB",
        "RLINKUP",
        "RLINKUPAFR",
        "RLINKUPAHR",
        "RLINKUPAWB",
        "RTTIINITMCS",
        "SCALLOC",
        "SCHO",
        "SCLD",
        "SCLDLOL",
        "SCLDSC",
        "SCLDLUL",
        "SDCCHUL",
        "SECTOR_ANGLE",
        "SIMSG1",
        "SIMSG7",
        "SIMSG8",
        "SLCA_BCCHACL",
        "SLCA_BCCHLVA",
        "SLCA_BTSPSTCHBPCACL",
        "SLCA_BTSPSTCHBPCLVA",
        "SLCA_TCHBPCACL",
        "SLCA_TCHBPCLVA",
        "SLCA_PSTCHACL",
        "SLCA_PSTCHLVA",
        "SLCA_PSSDCCHACL",
        "SLCA_PSSDCCHLVA",
        "SLCA_PSTCHBPCACL",
        "SLCA_PSTCHBPCLVA",
        "SLCA_CBCHACL",
        "SLCA_CBCHLVA",
        "SLCA_SDCCHACL",
        "SLCA_SDCCHLVA",
        "SLCA_STATE",
        "SLCA_TCHAMRFRACL",
        "SLCA_TCHAMRFRLVA",
        "SLCA_TCHAMRHRACL",
        "SLCA_TCHAMRHRLVA",
        "SLCA_TCHAMRWBACL",
        "SLCA_TCHAMRWBLVA",
        "SLCA_TCHEFRACL",
        "SLCA_TCHEFRLVA",
        "SLCA_TCHFRACL",
        "SLCA_TCHFRLVA",
        "SLCA_TCHHRACL",
        "SLCA_TCHHRLVA",
        "SLCA_BTSPSTCHACL",
        "SLCA_BTSPSTCHLVA",
        "SLCA_BTSPSSDCCHACL",
        "SLCA_BTSPSSDCCHLVA",
        "SLEVEL",
        "SLOW",
        "SPDCH",
        "SPRIO",
        "SSDESUL",
        "SSDESULAFR",
        "SSDESDL",
        "SSDESDLAFR",
        "SSDESDLAHR",
        "SSDESDLAWB",
        "SSDESULAHR",
        "SSDESULAWB",
        "SSEVALSD",
        "SSEVALSI",
        "SSLENSD",
        "SSLENSI",
        "SSOFFSETDL",
        "SSOFFSETDLAFR",
        "SSOFFSETDLAWB",
        "SSOFFSETUL",
        "SSOFFSETULAFR",
        "SSOFFSETULAWB",
        "SSRAMPSD",
        "SSRAMPSI",
        "SSTHRASSV",
        "SSTHRV",
        "SS_SDCCH_STATE",
        "SS_TCH_STATE",
        "STIME",
        "STREAMSUP",
        "T3212",
        "TALIM",
        "TCHFRUL",
        "TCHHRUL",
        "THRAV",
        "THRVP",
        "THRDV",
        "TIHO",
        "TMAXIHO",
        "TO",
        "TRAFBLK",
        "TSCSET1PAIRS",
        "TSS",
        "TX",
        "TXTYPE",
        "UMFI_ACTIVE",
        "UMFI_IDLE",
        "EARFCNIDLE",
        "EHPRIOTHR",
        "ELPRIOTHR",
        "EQRXLEVMIN",
        "ERATPRIO",
        "FDDARFCNIDLE",
        "GHPRIO",
        "GLPRIOTHR",
        "GMEASTHR",
        "GRATPRIO",
        "GTRES",
        "MINCHBW",
        "PCID",
        "PCIDG",
        "PCIDP",
        "PRIOCR",
        "UHPRIOTHR",
        "ULPRIOTHR",
        "UQRXLEVMIN",
        "URATPRIO",
        "VAMOSCELLSTATE",
        "VGCHALLOC",
        "VHOSUCCESS",
        "NUMINT",
        "DCDLACT",
        "DRX",
        "SPERIOD",
        "FSLOTS",
        "DLPCG",
        "DLPCE",
        "DLPCE2A",
        "INITDLPCG",
        "INITDLPCE",
        "INITDLPCE2A",
        "TBFULLIM",
        "TBFDLLIM",
        "FASTRETLTE",
        "COVERAGEE",
        "BCCHPS",
        "BCCHPSTYPE",
        "PRECCCH",
        "PRO",
        "DISABLEPERIODS",
        "COVERAGEU",
        "XRANGE",
        "EPUACT",
        "PUTHRESHU",
        "PUTHRESHL",
        "OSRTHRESH",
        "APSULPCACT",
        "SSDESGMSK",
        "SSDES8PSK",
        "SSDES16QAM"
    FROM
    ericsson_cnaiv2."internal_cell"

    """
)

msc = ReplaceableObject(
    'ericsson_cm_2g."MSC"',
    """

    SELECT 
        "FileName",
        "capabilities",
        "varDateTime",
        "subnetwork",
        "domain",
        "set",
        "USERDATA",
        "CAPLTCHEMER",
        "CELLCONNO",
        "CGIANTRNO",
        "DN",
        "EXPANDEDMNC",
        "LAI",
        "LOCARNO",
        "MSCG",
        "MSCPOOL_ID",
        "MSC_NAME",
        "NRIL",
        "NRIV",
        "OF_FF_E911ENH",
        "OF_MSCPOOL",
        "OF_MSCNF861",
        "VERSION",
        "ISMANAGED",
        "MESSAGE",
        "MSCBC",
        "CIPHERALGALLOW"
    FROM
    ericsson_cnaiv2."msc"

    """
)

nrel = ReplaceableObject(
    'ericsson_cm_2g."NREL"',
    """

    SELECT 
        "FileName",
        "capabilities",
        "varDateTime",
        "subnetwork",
        "domain",
        "set",
        "USERDATA",
        "BSC_NAME",
        "CELL_NAME",
        "NREL_NAME",
        "AWOFFSET",
        "BQOFFSET",
        "BQOFFSETAFR",
        "BQOFFSETAWB",
        "CAND",
        "CS",
        "GPRSVALID",
        "HIHYST",
        "KHYST",
        "KOFFSET",
        "LHYST",
        "LOHYST",
        "LOFFSET",
        "PROFFSET",
        "OFFSET",
        "TRHYST",
        "TROFFSET"
    FROM
    ericsson_cnaiv2."nrel"

    """
)

outer_cell = ReplaceableObject(
    'ericsson_cm_2g."OUTER_CELL"',
    """

    SELECT 
        "FileName",
        "capabilities",
        "varDateTime",
        "subnetwork",
        "domain",
        "set",
        "USERDATA",
        "CELL_NAME",
        "MSC_NAME",
        "N_MSC",
        "N_MSCG",
        "CI",
        "LAC",
        "MCC",
        "MNC",
        "NCS"
    FROM
    ericsson_cnaiv2."outer_cell"

    """
)

overlaid_cell = ReplaceableObject(
    'ericsson_cm_2g."OVERLAID_CELL"',
    """

    SELECT 
        "FileName",
        "capabilities",
        "varDateTime",
        "subnetwork",
        "domain",
        "set",
        "USERDATA",
        "BSC_NAME",
        "BSPWRMIN",
        "BSPWRT",
        "BSTXPWR",
        "CELL_NAME",
        "DTCB",
        "DTCBHYST",
        "IHO",
        "LCOMPDL",
        "LCOMPUL",
        "LOL",
        "LOLHYST",
        "MAXIHO",
        "MSTXPWR",
        "NDIST",
        "NNCELLS",
        "NUMINT",
        "QCOMPDL",
        "QCOMPUL",
        "QDESDL",
        "QDESDLAFR",
        "QDESDLAWB",
        "QDESUL",
        "QDESULAFR",
        "QDESULAWB",
        "QLIMDL",
        "QLIMDLAFR",
        "QLIMDLAWB",
        "QLIMUL",
        "QLIMULAFR",
        "QLIMULAWB",
        "QOFFSETDL",
        "QOFFSETDLAFR",
        "QOFFSETDLAWB",
        "QOFFSETUL",
        "QOFFSETULAFR",
        "QOFFSETULAWB",
        "SDCCHOL",
        "SLCA_TCHAMRHRACL",
        "SLCA_TCHAMRWBACL",
        "SLCA_TCHAMRHRLVA",
        "SLCA_TCHAMRWBLVA",
        "SLCA_BCCHACL",
        "SLCA_BCCHLVA",
        "SLCA_CBCHACL",
        "SLCA_CBCHLVA",
        "SLCA_STATE",
        "SLCA_SDCCHACL",
        "SLCA_SDCCHLVA",
        "SLCA_TCHEFRACL",
        "SLCA_TCHEFRLVA",
        "SLCA_TCHFRACL",
        "SLCA_TCHFRLVA",
        "SLCA_TCHHRACL",
        "SLCA_TCHHRLVA",
        "SLCA_TCHAMRFRACL",
        "SLCA_TCHAMRFRLVA",
        "SLCA_TCHBPCACL",
        "SLCA_TCHBPCLVA",
        "SSDESDL",
        "SSDESDLAFR",
        "SSDESUL",
        "SSDESULAFR",
        "SSDESULAWB",
        "SSOFFSETDL",
        "SSOFFSETDLAFR",
        "SSOFFSETDLAWB",
        "SSOFFSETUL",
        "SSOFFSETULAFR",
        "SSOFFSETULAWB",
        "SSDESDLAHR",
        "SSDESDLAWB",
        "SSDESULAHR",
        "QDESDLAHR",
        "QDESULAHR",
        "TAOL",
        "TAOLHYST",
        "TCHFROL",
        "TCHHROL",
        "TIHO",
        "TMAXIHO"
    FROM
    ericsson_cnaiv2."overlaid_cell"

    """
)

priority_profile = ReplaceableObject(
    'ericsson_cm_2g."PRIORITY_PROFILE"',
    """

    SELECT 
        "FileName",
        "capabilities",
        "varDateTime",
        "subnetwork",
        "domain",
        "set",
        "USERDATA",
        "BSC_NAME",
        "PRL1_INAC",
        "PRL2_INAC",
        "PRL3_INAC",
        "PRL4_INAC",
        "PRL5_INAC",
        "PRL6_INAC",
        "PRL7_INAC",
        "PRL8_INAC",
        "PRL9_INAC",
        "PRL10_INAC",
        "PRL11_INAC",
        "PRL12_INAC",
        "PRL13_INAC",
        "PRL14_INAC",
        "PRL15_INAC",
        "PRL16_INAC",
        "PRL1_PROBF",
        "PRL2_PROBF",
        "PRL3_PROBF",
        "PRL4_PROBF",
        "PRL5_PROBF",
        "PRL6_PROBF",
        "PRL7_PROBF",
        "PRL8_PROBF",
        "PRL9_PROBF",
        "PRL10_PROBF",
        "PRL11_PROBF",
        "PRL12_PROBF",
        "PRL13_PROBF",
        "PRL14_PROBF",
        "PRL15_PROBF",
        "PRL16_PROBF",
        "PRI_PROFILE_NAME"
    FROM
    ericsson_cnaiv2."priority_profile"

    """
)

site = ReplaceableObject(
    'ericsson_cm_2g."SITE"',
    """

    SELECT 
        "FileName",
        "capabilities",
        "varDateTime",
        "subnetwork",
        "domain",
        "set",
        "USERDATA",
        "ALTITUDE",
        "BSC_NAME",
        "LATITUDE",
        "LONGITUDE",
        "NOTE",
        "SITE_NAME"
    FROM
    ericsson_cnaiv2."site"

    """
)

tg = ReplaceableObject(
    'ericsson_cm_2g."TG"',
    """

    SELECT 
        "FileName",
        "capabilities",
        "varDateTime",
        "subnetwork",
        "domain",
        "set",
        "USERDATA",
        "BSC_NAME",
        "SITE_NAME",
        "TG_NAME"
    FROM
    ericsson_cnaiv2."tg"

    """
)

utran_external_cell = ReplaceableObject(
    'ericsson_cm_2g."UTRAN_EXTERNAL_CELL"',
    """

    SELECT 
        "FileName",
        "capabilities",
        "varDateTime",
        "subnetwork",
        "domain",
        "set",
        "USERDATA",
        "BSC_NAME",
        "CELL_NAME",
        "CI",
        "FDDARFCN",
        "LAC",
        "MRSL",
        "MCC",
        "MNC",
        "RNCID",
        "SCRCODE",
        "USEDFREQTHRESH2DECNO"
    FROM
    ericsson_cnaiv2."utran_external_cell"

    """
)

utran_nrel = ReplaceableObject(
    'ericsson_cm_2g."UTRAN_NREL"',
    """

    SELECT 
        "FileName",
        "capabilities",
        "varDateTime",
        "subnetwork",
        "domain",
        "set",
        "USERDATA",
        "BSC_NAME",
        "CELL_NAME",
        "NREL_NAME"
    FROM
    ericsson_cnaiv2."utran_nrel"

    """
)


def upgrade():
    op.create_view(bsc)
    op.create_view(channel_group)
    op.create_view(external_cell)
    op.create_view(inner_cell)
    op.create_view(internal_cell)
    op.create_view(msc)
    op.create_view(nrel)
    op.create_view(outer_cell)
    op.create_view(overlaid_cell)
    op.create_view(priority_profile)
    op.create_view(site)
    op.create_view(tg)
    op.create_view(utran_external_cell)
    op.create_view(utran_nrel)


def downgrade():
    op.drop_view(bsc)
    op.drop_view(channel_group)
    op.drop_view(external_cell)
    op.drop_view(inner_cell)
    op.drop_view(internal_cell)
    op.drop_view(msc)
    op.drop_view(nrel)
    op.drop_view(outer_cell)
    op.drop_view(overlaid_cell)
    op.drop_view(priority_profile)
    op.drop_view(site)
    op.drop_view(tg)
    op.drop_view(utran_external_cell)
    op.drop_view(utran_nrel)

