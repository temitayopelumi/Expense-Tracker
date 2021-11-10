<template>
  <v-app>
    <v-main> <AddExpense /></v-main>
    <BottomBar />
  </v-app>
</template>

<script>
import BottomBar from "./components/BottonBar";
import AddExpense from "./components/AddExpense";
export default {
  name: "App",
  components: {
    BottomBar,
    AddExpense,
  },

  data: () => ({}),
};
</script>
