<template>
    <div>
        <div class="sample-list">
            <v-row>
                <v-col
                    v-for="sample in samples"
                    :key="sample.id"
                    cols="12"
                    lg="3"
                    md="4"
                    sm="6"
                    xs="12"
                >
                    <SampleCard
                        :id="sample.id"
                        :name="sample.name"
                        :tempo="sample.tempo"
                        :_key="sample.key"
                        :_mode="sample.mode"
                        :duration="sample.duration"
                        :tags="sample.tags"
                        :userId="sample.user.id"
                        :username="sample.user.username"
                    />
                </v-col>
            </v-row>
        </div>
        <v-btn
            fab
            fixed
            bottom
            :disabled="stopAllDisabled"
            color="error"
            @click="stopAll"
            :style="{left: '50%', transform:'translateX(-50%)'}"
        >
            <v-icon>mdi-stop</v-icon>
        </v-btn>
    </div>
</template>

<script>
import SampleCard from '~/components/SampleCard.vue'

export default {
    components: {
        SampleCard
    },

    props: ['samples'],

    data () {
        return {
            numberPlaying: 0
        }
    },

    computed: {
        stopAllDisabled () {
            return this.numberPlaying < 1
        }
    },

    mounted () {
        this.$nuxt.$on('samplePlay', () => {
            ++this.numberPlaying
        })

        this.$nuxt.$on('samplePause', () => {
            --this.numberPlaying
        })
    },

    methods: {
        stopAll() {
            this.$nuxt.$emit('sampleStopAll')
        }
    }
}
</script>

<style>
.sample .v-btn__content {
    text-transform: none !important;
}
</style>
