<template>
  <div>
     <h1 class="mb-8 font-bold text-3xl">Dashboard</h1>
    <p class="mb-12 leading-normal">Hey there! Welcome to Ping CRM, a demo app designed to help illustrate how <a class="text-indigo-500 underline hover:text-orange-600" href="https://github.com/inertiajs">Inertia.js</a> works.</p>
    <div>
      <inertia-link class="btn-indigo" href="/500">500 error</inertia-link>
      <inertia-link class="btn-indigo" href="/404">404 error</inertia-link>
    </div>
    <h2 class="page-title">Contacts</h2>
    <ul>
      <li :key="contact.id" v-for="contact in contact_list">
        <inertia-link class="font-black" :href="'/contact/' + contact.id">
          {{contact.name}}
        </inertia-link>
      </li>
    </ul>
  </div>
</template>

<script>

import Layout from '../Shared/Layout'

export default {
  name:'Index',
  layout:Layout
};
</script>