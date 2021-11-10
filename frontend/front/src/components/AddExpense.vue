<template>
  <v-form v-model="valid">
    <v-container fluid>
      <v-row>
        <v-col cols="4">
          <v-subheader>Prefix for dollar currency</v-subheader>
        </v-col>
        <v-col cols="8">
          <v-text-field
            label="Amount"
            value="10.00"
            prefix="$"
            required
          ></v-text-field>
        </v-col>
      </v-row>
    </v-container>
  </v-form>
</template>
<script>
export default {
  data: () => ({
    valid: false,
    firstname: "",
    lastname: "",
    nameRules: [
      (v) => !!v || "Name is required",
      (v) => v.length <= 10 || "Name must be less than 10 characters",
    ],
    email: "",
    emailRules: [
      (v) => !!v || "E-mail is required",
      (v) => /.+@.+/.test(v) || "E-mail must be valid",
    ],
  }),
};
</script>