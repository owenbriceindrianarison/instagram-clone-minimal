import { createAsyncThunk, createSlice, PayloadAction } from '@reduxjs/toolkit'
import { RootState } from '../../app/store'
import { sendLogin } from './authAPI'

export interface AuthState {
  user: {
    authToken: string
    authTokenType: string
    userId: number | undefined
    username: string
  }
  status: 'idle' | 'loading' | 'failed'
}

const initialState: AuthState = {
  user: {
    authToken: '',
    authTokenType: '',
    userId: undefined,
    username: '',
  },
  status: 'idle',
}

// The function below is called a thunk and allows us to perform async logic. It
// can be dispatched like a regular action: `dispatch(incrementAsync(10))`. This
// will call the thunk with the `dispatch` function as the first argument. Async
// code can then be executed and other actions can be dispatched. Thunks are
// typically used to make async requests.
export const loginAsync = createAsyncThunk(
  'auth/sendLogin',
  async (form: any) => {
    const response = await sendLogin(form)
    return response.data
  }
)

export const authSlice = createSlice({
  name: 'auth',
  initialState,
  // The `reducers` field lets us define reducers and generate associated actions
  reducers: {
    logoutUser: (state) => {
      state.user = {
        authToken: '',
        authTokenType: '',
        userId: undefined,
        username: '',
      }
    },
  },

  extraReducers: (builder) => {
    builder
      .addCase(loginAsync.pending, (state) => {
        state.status = 'loading'
      })
      .addCase(loginAsync.fulfilled, (state, action) => {
        state.status = 'idle'
        console.log({ action })
        state.user = {
          authToken: action.payload.access_token,
          authTokenType: action.payload.token_type,
          userId: action.payload.user_id,
          username: action.payload.username,
        }
      })
  },
})

export const { logoutUser } = authSlice.actions

export const selectUser = (state: RootState) => state.auth.user

export default authSlice.reducer
