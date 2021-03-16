import React, { Component } from 'react';
import { Dropdown, DropdownToggle, DropdownMenu, DropdownItem } from 'reactstrap';
import {Link} from "react-router-dom";

const defaultAvatar = require("assets/img/avatar-placeholder.png");


class Navbar extends Component {
    constructor(props) {
        super(props);
        this.state = {dropdownOpen: false};
    }

    toggle = () => {
        this.setState({dropdownOpen: !this.state.dropdownOpen});
    };
    render() {
        const { navToggle, logOut, user, perfil } = this.props;
        return (
            <nav className="align-items-stretch flex-md-nowrap p-0 navbar navbar-light">
                <div className="main-navbar__search w-100 d-none d-md-flex d-lg-flex">
                    <div className="ml-3 input-group input-group-seamless" />
                </div>
                <ul className="border-left flex-row navbar-nav">
                    <Dropdown isOpen={this.state.dropdownOpen} toggle={this.toggle}>
                        <DropdownToggle color="light" caret className="nav-item-dropdown border-0">
                            <img className="user-avatar rounded-circle mr-3"
                                 src={(perfil && perfil.avatar) ? perfil.avatar : defaultAvatar}
                                 alt="User Avatar" />
                            <span className="d-none d-md-inline-block">{user.first_name}</span>
                        </DropdownToggle>
                        <DropdownMenu>
                            <DropdownItem header>Usuario</DropdownItem>
                            <DropdownItem>
                                <Link tabIndex="0"
                                   to="/user-profile">
                                    <i className="material-icons"></i>
                                    Profile
                                </Link>
                            </DropdownItem>
                            <DropdownItem>
                                <Link tabIndex="0"
                                   to="/cambiocontrasenia">
                                    <i className="material-icons">vpn_key</i>
                                    Contraseña
                                </Link>
                            </DropdownItem>
                            <DropdownItem divider />
                            <DropdownItem>
                                <Link tabIndex="0" className="text-danger" onClick={logOut} to="/login">
                                    <i className="material-icons text-danger"></i>
                                    Logout
                                </Link>
                            </DropdownItem>
                        </DropdownMenu>
                    </Dropdown>
                </ul>
                <nav className="nav">
                    <a  className="nav-link nav-link-icon toggle-sidebar d-sm-inline d-md-inline d-lg-none text-center"
                        onClick={ navToggle } >
                        <i className="material-icons"></i>
                    </a>
                </nav>
            </nav>
        );
    }
}

export default Navbar;
