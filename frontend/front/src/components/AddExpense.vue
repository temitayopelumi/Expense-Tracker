<template>
  <v-card dark>
    <v-card-title>
      <span class="text-h5" color="primary">Add Transaction</span>
    </v-card-title>
    <v-card-text>
      <v-form>
        <v-container fluid>
          <v-row>
            <v-col cols="5">
              <v-subheader>Category</v-subheader>
            </v-col>
            <v-col cols="7">
              <v-autocomplete
                v-model="values"
                :items="items"
                solo
              ></v-autocomplete>
            </v-col>
          </v-row>
          <v-row>
            <v-col cols="5">
              <v-subheader>Amount</v-subheader>
            </v-col>
            <v-col cols="7">
              <v-text-field
                value=""
                dense
                outlined
                prefix="$"
                required
              ></v-text-field>
            </v-col>
          </v-row>
          <v-row>
            <v-col cols="5">
              <v-subheader>Type</v-subheader>
            </v-col>
            <v-col cols="7">
              <v-autocomplete
                v-model="type_values"
                :items="type"
                solo
              ></v-autocomplete>
            </v-col>
          </v-row>
          <v-row>
            <v-col cols="5">
              <v-subheader>Date</v-subheader>
            </v-col>
            <v-col cols="7">
              <v-dialog
                ref="dialog"
                v-model="modal"
                :return-value.sync="date"
                persistent
                width="290px"
              >
                <template v-slot:activator="{ on, attrs }">
                  <v-text-field
                    v-model="date"
                    prepend-icon="mdi-calendar"
                    readonly
                    dense
                    outlined
                    v-bind="attrs"
                    v-on="on"
                  ></v-text-field>
                </template>
                <v-date-picker v-model="date" scrollable>
                  <v-spacer></v-spacer>
                  <v-btn text color="primary" @click="modal = false">
                    Cancel
                  </v-btn>
                  <v-btn text color="primary" @click="$refs.dialog.save(date)">
                    OK
                  </v-btn>
                </v-date-picker>
              </v-dialog>
            </v-col>
          </v-row>
          <v-row>
            <v-col cols="5">
              <v-subheader>Name</v-subheader>
            </v-col>
            <v-col cols="7">
              <v-text-field dense outlined required></v-text-field>
            </v-col>
          </v-row>
          <v-row>
            <v-col cols="5"></v-col>
            <v-col cols="2"
              ><v-btn class="mx-2" fab small color="primary">
                <v-icon dark>mdi-check </v-icon>
              </v-btn></v-col
            >
            <v-col cols="5"></v-col>
          </v-row>
        </v-container>
      </v-form>
    </v-card-text>
  </v-card>
</template>
<script>
export default {
  data: () => ({
    date: new Date(Date.now() - new Date().getTimezoneOffset() * 60000)
      .toISOString()
      .substr(0, 10),
    menu: false,
    modal: false,
    menu2: false,
    items: ["Grocery", "Clothing", "Travel", "Rent"],
    values: ["grocery", "clothing", "travel", "rent"],
    type: ["Expense", "Income"],
    type_values: ["expense", "income"],
    value: null,
  }),
};
</script>