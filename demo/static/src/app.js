import { InertiaApp } from '@inertiajs/inertia-vue'
import Vue from 'vue'
import axios from "axios";
import PortalVue from 'portal-vue'

axios.defaults.xsrfCookieName = "csrftoken";
axios.defaults.xsrfHeaderName = "X-CSRFToken";

Vue.config.productionTip = true;

Vue.use(InertiaApp);
Vue.use(PortalVue);

let customRoute = (...args) => {
    args[0] = 'demo:' + args[0];
    return window.reverseUrl(...args);
}

Vue.mixin({ methods: { route: customRoute } });

const app = document.getElementById('app');
// we are getting the initialPage from a rendered json_script
const page = JSON.parse(document.getElementById("page").textContent);

import Index from "./Pages/Dashboard/Index";
import Organization from "./Pages/Organizations/Index";
import OrganizationEdit from "./Pages/Organizations/Edit";
import OrganizationCreate from "./Pages/Organizations/Create";
import Contacts from "./Pages/Contacts/Index";
import ContactCreate from "./Pages/Contacts/Create";
import ContactEdit from "./Pages/Contacts/Edit";
import Login from "./Pages/Auth/Login";

const pages = {
  'Login': Login,
  'Index': Index,
  'Contacts': Contacts,
  'Contacts.Edit': ContactEdit,
  'Contacts.Create': ContactCreate,
  'Organizations': Organization,
  "Organizations.Edit": OrganizationEdit,
  "Organizations.Create": OrganizationCreate
}

new Vue({
  render: h => h(InertiaApp, {
    props: {
      initialPage: page,
      resolveComponent: (name) => {
        console.log("resolveComponent ", name, pages[name])
        return pages[name];
      },
    },
  }),
}).$mount(app)
