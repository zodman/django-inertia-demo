<template>
  <Layout>
    <h2 class="page-title">Contacts</h2>
    <ul>
      <li :key="contact.id" v-for="contact in contact_list">
        <inertia-link class="font-black" :href="'/contact/' + contact.id">
          {{contact.name}}
        </inertia-link>
      </li>
    </ul>
  </Layout>
</template>

<script>
import { InertiaLink } from "@inertiajs/inertia-vue";
export default {
  props: ["contact_list", "shared"],
  components: { InertiaLink }
};
</script>