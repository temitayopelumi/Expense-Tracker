<template>
  <v-bottom-navigation :value="value" color="primary">
    <v-row>
      <v-col cols="1"></v-col>
      <v-col cols="2">
        <v-btn color="white">
          <span>Home</span>
          <v-icon x-large>mdi-home</v-icon>
        </v-btn>
      </v-col>
      <v-col cols="2"></v-col>
      <v-col cols="2">
        <v-btn color="white">
          <span>Book</span>

          <v-icon x-large>mdi-plus</v-icon>
        </v-btn>
      </v-col>
      <v-col cols="2"></v-col>
      <v-col cols="2">
        <v-btn color="white">
          <span>Setting</span>
          <v-icon x-large>mdi-account</v-icon>
        </v-btn>
      </v-col>
      <v-col cols="1"></v-col>
    </v-row>
  </v-bottom-navigation>
</template>
<script>
export default {
  data: () => ({ value: 1 }),
};
</script>