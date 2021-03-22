import CicloListar from "./CicloListar";
import { connect } from "react-redux";
import { actions } from "../../../redux/modules/ciclo/ciclo";

const ms2p = (store) => {
    return {
        ...store.ciclo,
    };
};

const md2p = {
    ...actions,
};

export default connect(ms2p, md2p)(CicloListar);
